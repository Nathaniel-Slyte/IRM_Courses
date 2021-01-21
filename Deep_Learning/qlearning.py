from tqdm import tqdm
from time import sleep

import gym
import numpy as np


# ====== Hyperparameters
STEPS = 1_000  # Number of Step to Train
α = 0.5        # Learning Rate
γ = 0.99       # Discount Factor
ε = 1.0        # Greedy Parameter (Exploration VS Exploitation)

# ====== Chose Environment
env = gym.make("Taxi-v3")

# ====== Q Matrix
Q = np.zeros((env.observation_space.n, env.action_space.n))
Q.fill(5)  # Optimistic Start (Encourage Exploration)

# ====== Bellman Equation Based Iterative Update
with tqdm(range(STEPS), "Iteration") as pbar:
    for step in pbar:
        s, done = env.reset(), False  # Retrieve s0, Game Done?
        while not done:
            ε_ = (1 - (step / STEPS) ** 4) * ε
            pbar.set_postfix(ε=ε_)
            a = env.action_space.sample() if np.random.uniform(0, 1) < ε_ else np.argmax(Q[s])  # Chose a_t
            s_next, r, done, *_ = env.step(a)                                               # Retrieve s_t+1, r_t+1 given s_t, a_t
            Q[s, a] = (1 - α) * Q[s, a] + α * (r + γ * np.max(Q[s_next]))                   # Bellman Equation
            s = s_next                                                                      # s_t = s_t+1

# ====== Test Environment
for i in range(10):
    print(f"\n====== TEST[{i+1:02d}/{10}]")
    s = env.reset()
    done = False
    while not done:
        s, _, done, *_ = env.step(np.argmax(Q[s]))
        env.render()
        sleep(1)
env.close()