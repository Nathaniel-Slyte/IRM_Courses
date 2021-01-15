from __future__ import annotations

from dataclasses import dataclass
from PIL import Image
from torch.autograd import Variable
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from typing import Dict, List, NamedTuple, Tuple

import numpy as np
import os
import torch
import torch.nn as nn
import torchvision.transforms as T


class Pokemon(NamedTuple):
    name: str
    ptype: str
    path: str


@dataclass
class Pokedex:
    pokemons: List[Pokemon]
    ptype2id: Dict[str, int]
    id2ptype: Dict[int, str]

    def __len__(self) -> int:
        return len(self.pokemons)

    def __getitem__(self, idx: int) -> Pokemon:
        return self.pokemons[idx]

    @classmethod
    def load(cls, path: str) -> Pokedex:
        listdir_join = lambda p: [os.path.join(p, f) for f in os.listdir(p)]
        pokemon_folders = listdir_join(path)

        pokemons, ptypes = [], []
        for pokemon_folder in pokemon_folders:
            pokemon_files = listdir_join(pokemon_folder)
            
            ptype = pokemon_folder.split("/")[-1]
            ptypes.append(ptype)
            
            for pokemon_file in pokemon_files:
                pokemons.append(Pokemon(
                    pokemon_file.split("/")[-1].split(".")[0],
                    ptype,
                    pokemon_file,
                ))

        ptype2id = {p: i for i, p in enumerate(ptypes)}
        id2ptype = {i: p for i, p in enumerate(ptypes)}

        return cls(pokemons, ptype2id, id2ptype)


class Pokeset(Dataset):
    def __init__(self, pokedex: Pokedex, size: int) -> None:
        super(Pokeset, self).__init__()
        self.pokedex = pokedex
        self.transforms = T.Compose([
            T.Resize(size),
            T.CenterCrop(size),
            T.ToTensor(),
            T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])

    def __len__(self) -> int:
        return len(self.pokedex)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, int]:
        pokemon = self.pokedex[idx]
        
        image = Image.open(pokemon.path).convert("RGBA")
        image = np.array(image)
        r, g, b, a = np.rollaxis(image, axis=-1)
        r[a == 0] = 0
        g[a == 0] = 0
        b[a == 0] = 0
        image = np.dstack([r, g, b])
        image = Image.fromarray(image)

        ptype = self.pokedex.ptype2id[pokemon.ptype]
        return self.transforms(image), ptype


class VanillaPokeGenerator(nn.Module):
    def __init__(self, z_dim: int) -> None:
        super(VanillaPokeGenerator, self).__init__()
        self.mapping = nn.Linear(z_dim, 512 * 8 * 8)
        self.decoder = nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.Conv2d(512, 256, kernel_size=5, stride=1, padding=2, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),

            nn.Upsample(scale_factor=2),
            nn.Conv2d(256, 128, kernel_size=5, stride=1, padding=2, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),

            nn.Upsample(scale_factor=2),
            nn.Conv2d(128, 64, kernel_size=5, stride=1, padding=2, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),

            nn.Conv2d(64, 3, kernel_size=5, stride=1, padding=2, bias=False),
            nn.Tanh(),
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        z = self.mapping(z).view(z.size(0), 512, 8, 8)
        y = self.decoder(z)
        return y


class VanillaPokeDiscriminator(nn.Module):
    def __init__(self) -> None:
        super(VanillaPokeDiscriminator, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=7, stride=4, padding=3, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(32, 64, kernel_size=5, stride=2, padding=2, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(64, 128, kernel_size=5, stride=2, padding=2, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(128, 256, kernel_size=5, stride=2, padding=2, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(256, 512, kernel_size=5, stride=2, padding=2, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(512, 1, kernel_size=1, stride=1, padding=0, bias=False),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        y = self.features(x)
        return y.view(x.size(0), 1)


if __name__ == "__main__":
    DATA = "./dataset" # Do not Touch
    SIZE = 64          # Do not Touch
    
    BATCH_SIZE = 64
    NUM_WORKERS = 6

    Z_DIM = 32

    EPOCHS = 100
    LR = 1e-3
    BETAS = 0.5, 0.9


    pokedex = Pokedex.load(DATA)
    pokeset = Pokeset(pokedex, size=SIZE)
    
    loader = DataLoader(
        pokeset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=True,
    )


    def weight_init(module: nn.Module) -> None:
        if isinstance(module, nn.Conv2d):
            module.weight.data.normal_(0.0, 0.02)
        elif isinstance(module, nn.BatchNorm2d):
            module.weight.data.normal_(0.0, 0.02)
            module.bias.data.fill_(0.0)


    generator = VanillaPokeGenerator(Z_DIM).apply(weight_init).cuda()
    optim_g = AdamW(generator.parameters(), lr=LR, betas=BETAS)

    discriminator = VanillaPokeDiscriminator().apply(weight_init).cuda()
    optim_d = AdamW(discriminator.parameters(), lr=LR, betas=BETAS)
    
    criterion = nn.BCELoss().cuda()

    vz = torch.randn(4 * 4, Z_DIM).cuda()
    device = vz.device

    for epoch in tqdm(range(EPOCHS), "Epoch"):

        with tqdm(loader, f"Train [{epoch + 1}/{EPOCHS}]") as pbar:
            total_gene_loss = 0.0
            total_real_loss = 0.0
            total_fake_loss = 0.0

            discriminator.train()
            generator.train()
            for image, ptype in pbar:
                image, ptype = image.cuda(), ptype.cuda()
                B, *_ = image.size()
                
                # Train Discriminator
                optim_d.zero_grad()

                pred_real = discriminator(image)
                real_targets = torch.rand(B, 1, device=device)
                real_targets = 0.1 * real_targets
                loss_real = criterion(pred_real, real_targets)

                z = torch.randn(B, Z_DIM, device=device)
                fake = generator(z)
                pred_fake = discriminator(fake)
                fake_targets = torch.rand(B, 1, device=device)
                fake_targets = 0.1 * fake_targets + 0.9
                loss_fake = criterion(pred_fake, fake_targets)

                loss = loss_real + loss_fake
                loss.backward()
                optim_d.step()

                total_real_loss += torch.mean(loss_real).item() / len(loader)
                total_fake_loss += torch.mean(loss_fake).item() / len(loader)

                # Train Generator
                optim_g.zero_grad()
                
                z = torch.randn(B, Z_DIM, device=device)
                fake = generator(z)
                pred_fake = discriminator(fake)
                targets = torch.zeros(B, 1, device=device)
                loss = criterion(pred_fake, targets)

                loss.backward()
                optim_g.step()
                
                total_gene_loss += loss.item() / len(loader)

                pbar.set_postfix(
                    D_real=total_real_loss,
                    D_fake=total_fake_loss,
                    G=total_gene_loss,
                )

        with torch.no_grad():
            generator.eval()
            vfake = generator(vz)
            vfake = vfake.squeeze(0).permute(0, 2, 3, 1)
            vfake = (vfake * 0.5) + 0.5
            vfake = vfake.clamp(0, 1)
            vfake = vfake.cpu().numpy()
            vfake = np.vstack([np.hstack(vfake[i*4:i*4+4]) for i in range(4)])
            vfake = (vfake * 255).astype(np.uint8)
            image = Image.fromarray(vfake)
            image.show(title=f"Epoch {epoch + 1}")
            image.save("pokemons.png")

        trace = torch.jit.trace(generator, vz)
        torch.jit.save(trace, "pokegan.ts")