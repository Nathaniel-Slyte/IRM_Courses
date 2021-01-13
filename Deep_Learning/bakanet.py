from torch.utils.data import DataLoader, random_split
from torch.optim import SGD
from torchvision.datasets.cifar import CIFAR10
from tqdm import tqdm

import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as T


class BakaNet(nn.Module):
    """Model

    The Model Class Can be Modified.
    However, the `forward` arguments and output must stay unchanged.
    The model take a Batch of Images (B, C, H, W) as inputs and output a
    tensor of size (B, N_CLASSES).
    The `argmax` of the output tensor is used to compute final accuracy.
    """

    def __init__(self, features: int, hidden: int, n_classes: int) -> None:
        super(BakaNet, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(features, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, n_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layers(x.view(x.size(0), -1))


if __name__ == '__main__':
    # This 2 lines must stay unchanged
    np.random.seed(42)
    torch.manual_seed(42)

    
    # Replace by your own Name and SURNAME, else 0
    NAME = "Baka"
    SURNAME = "NET"

    # Those constants must stay unchanged, the inform of dataset ins and outs
    CIFAR10_SIZE = 32
    CIFAR10_CHANNELS = 3
    CIFAR10_CLASSES = 10

    # Those parameters can be changed depending on your pc architecture
    BATCH_SIZE = 32
    NUM_WORKERS = 4

    # Those parameters can be modified, deleted.
    HIDDEN = 512
    EPOCHS = 15
    LR = 1e-3


    # Load Dataset and Download if does not exists yet
    cifar10 = CIFAR10(
        root="./dataset", train=True, transform=T.ToTensor(), download=True,
    )

    # Split dataset into Trainset and Validset (Do not Use a Testset)
    trainlen = int(0.8 * len(cifar10))
    validlen = len(cifar10) - trainlen
    trainset, validset = random_split(cifar10, lengths=[trainlen, validlen])

    # Data Loaders
    trainloader = DataLoader(
        trainset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=True,
    )
    validloader = DataLoader(
        validset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True,
    )

    # Creration of the Model and Cirterion (Pushed to GPU side)
    model = BakaNet(
        CIFAR10_SIZE * CIFAR10_SIZE * CIFAR10_CHANNELS,
        HIDDEN,
        CIFAR10_CLASSES,
    ).cuda()
    criterion = nn.CrossEntropyLoss().cuda()

    # Optimizer
    optim = SGD(model.parameters(), lr=LR)

    # Training Pipeline
    for epoch in tqdm(range(EPOCHS), desc="Epoch"):
        # Training stage
        total_loss = 0.0
        total_acc = 0.0
        
        model = model.train()
        with tqdm(trainloader, "Train") as pbar:
            for inputs, labels in pbar:
                # Push Batch Data to GPU and Reset Gradients
                inputs, labels = inputs.cuda(), labels.cuda()
                optim.zero_grad()

                # Compute Outputs, Loss and Backward Gradients
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optim.step()
                
                # Display Total Loss and Accuracy during Training
                total_loss += loss.item() / len(trainloader)
                total_acc += (
                    (torch.argmax(outputs, 1) == labels).sum().item() /
                    len(trainset)
                )
                pbar.set_postfix(
                    loss=total_loss, acc=f"{total_acc * 100:.2f}%",
                )

        # Validation Stage (no_grad used to avoid wasting memory for gradients)
        with torch.no_grad():
            total_loss = 0.0
            total_acc = 0.0

            model = model.eval()
            with tqdm(validloader, "Valid") as pbar:
                for inputs, labels in pbar:
                    # Push Batch Data to GPU
                    inputs, labels = inputs.cuda(), labels.cuda()
                    
                    # Compute Outputs, Loss
                    outputs = model(inputs)
                    loss = criterion(outputs, labels)

                    # Display Total Loss and Accuracy during Validation
                    total_loss += loss.item() / len(validloader)
                    total_acc += (
                        (torch.argmax(outputs, 1) == labels).sum().item() /
                        len(validset)
                    )
                    pbar.set_postfix(
                        loss=total_loss, acc=f"{total_acc * 100:.2f}%",
                    )

    # This code must stay unchanged, it is responsible for saving the model
    model = model.eval()
    trace = torch.jit.trace(
        model.cpu(),
        torch.rand((1, CIFAR10_CHANNELS, CIFAR10_SIZE, CIFAR10_SIZE)),
    )
    torch.jit.save(trace, f"Challenge01_{NAME}_{SURNAME}.ts")