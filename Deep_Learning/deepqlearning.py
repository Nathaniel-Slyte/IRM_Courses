from itertools import count
from tqdm import tqdm
from typing import List, NamedTuple
from torch.optim import AdamW

import gym
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as T


class Transition(NamedTuple):
    s: torch.Tensor
    a: torch.Tensor
    s_next: torch.Tensor
    r: torch.Tensor


class ReplayMemory:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.memory: List[Transition] = []
        self.idx = 0

    def __len__(self) -> int:
        return len(self.memory)

    def push(self, transition: Transition) -> None:
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.idx] = transition
        self.idx = (self.idx + 1) % self.capacity

    def sample(self, batch_size: int) -> List[Transition]:
        idxs = np.random.choice(len(self.memory), size=batch_size)
        return [self.memory[idx] for idx in idxs]


class QNet(nn.Module):
    def __init__(self, actions: int) -> None:
        super(QNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=7, stride=4),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.Conv2d(16, 32, kernel_size=5, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 32, kernel_size=5, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
        )
        self.fc = nn.Sequential(
            nn.Linear(32 * 5 * 5, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, actions)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)


def get_screen(env: gym.Env) -> torch.Tensor:
    render = env.render(mode="rgb_array").transpose((2, 0, 1))
    render = torch.from_numpy(render.astype(np.float32) / 255.0)
    render = render.unsqueeze(0)
    B, C, H, W = render.size()
    render = T.functional.center_crop(render, (min(W, H), min(W, H)))
    render = T.functional.resize(render, (int(0.3 * min(W, H)), int(0.3 * min(W, H))))
    return render


DEVICE = "cuda"
EPISODES = 1_000
CAPACITY = 10_000
BATCH_SIZE = 32
α = 1e-3
γ = 0.99
ε = 1.0
ε_decay = 0.999

env = gym.make("CartPole-v1")

q_network = QNet(actions=env.action_space.n).to(DEVICE)
replay_memory = ReplayMemory(capacity=CAPACITY)
optim = AdamW(q_network.parameters(), lr=α)

# ====== Train Model
history = []

with tqdm(range(EPISODES), "Episode") as pbar:
    for epsode in pbar:
        env.reset()   # Reset Environment
        done = False  # Is Game Done?

        last_screen = get_screen(env)                  # Screen t-1
        current_screen = get_screen(env)               # Screen t
        s = (current_screen - last_screen).to(DEVICE)  # Compute State t

        # ====== While Episode
        for t in count():
            # Explore or Exploit
            with torch.no_grad():
                a = (
                    torch.tensor([[np.random.randint(env.action_space.n)]]).long().to(DEVICE)
                    if np.random.uniform(0, ε) else torch.argmax(q_network(s), dim=1).view(1, 1)
                )
            
            # Collect Reward
            _, r, done, *_ = env.step(a.item())
            r = torch.tensor([r]).to(DEVICE)

            last_screen = current_screen                                               # Screen t-1 = Screen t
            current_screen = get_screen(env)                                           # Screen t   = Screen t+1
            s_next = (current_screen - last_screen).to(DEVICE) if not done else None   # Compute State t+1

            replay_memory.push(Transition(s, a, s_next, r))  # Add Transition to Replay Memory
            s = s_next                                       # State t = State t+1

            # ====== Optimize Model
            if len(replay_memory) >= BATCH_SIZE:
                # Sample Transitions
                transitions = replay_memory.sample(BATCH_SIZE)

                # Fuse Transition for Batch
                batch = Transition(*zip(*transitions))
                batch_s = torch.cat(batch.s)            # Fuse State for Batch
                batch_a = torch.cat(batch.a)            # Fuse Action for Batch
                batch_r = torch.cat(batch.r)            # Fuse Reward for Batch

                nf = lambda s: s is not None
                nf_mask = torch.tensor(list(map(nf, batch.s_next))).bool().to(DEVICE)  # Create Non-Final Mask
                nf_s_next = torch.cat(list(filter(nf, batch.s_next))).to(DEVICE)       # Collect Non-Final Next State

                # Compute Actual Q Values Estimations
                q_values = q_network(batch_s).gather(1, batch_a)

                # Compute Expected Q Values Estimations
                q_values_next = torch.zeros(BATCH_SIZE).to(DEVICE)
                q_values_next[nf_mask] = q_network(nf_s_next).max(dim=1)[0]
                𝔼_q_values = (batch_r + γ * q_values_next).unsqueeze(1)

                # Optimization Process
                optim.zero_grad()
                loss = F.mse_loss(q_values, 𝔼_q_values)
                loss.backward()
                for parameter in q_network.parameters():
                    parameter.grad.data.clamp_(-1, 1)
                optim.step()

            if done:
                history.append(t + 1)
                break

        # Update Greedy Epsilon
        ε *= ε_decay
        pbar.set_postfix(ε=ε)


plt.plot(history)
plt.show()

torch.jit.save(torch.jit.trace(q_network, batch_s), "dqn.ts")

#====== Test Model
q_network.eval()

for i in range(10):
    print(f"\n====== TEST[{i+1:02d}/{10}]")
    env.reset()
    done = False

    last_screen = get_screen(env)
    current_screen = get_screen(env)
    s = (current_screen - last_screen).to(DEVICE)

    while not done:
        with torch.no_grad():
            a = torch.argmax(q_network(s), dim=1).item()
        _, _, done, *_ = env.step(a)
        
        last_screen = current_screen
        current_screen = get_screen(env)
        s = (current_screen - last_screen).to(DEVICE) if not done else None
        
        env.render()
env.close()