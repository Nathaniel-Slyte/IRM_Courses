from __future__ import annotations

from dataclasses import dataclass
from num2words import num2words
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from torchtext.data import get_tokenizer
from tqdm import tqdm
from typing import Dict, List, Set, Tuple

import torch
import torch.nn as nn


@dataclass
class HarryPotterBooks:
    path: str
    raw: str
    tokens: List[str]
    vocab: Set[str]
    word2id: Dict[str, int]
    id2word: Dict[int, str]

    @classmethod
    def from_file(cls, path: str, fraction: float = 1) -> HarryPotterBooks:
        with open(path, "r") as f:
            raw = f.read()
            raw = " ".join(raw.split())

        numbers = lambda t: num2words(t) if type(t) in [int, float] else t
        tokenizer = get_tokenizer("basic_english")
        tokens = tokenizer(raw)
        tokens = list(map(numbers, tokens))
        tokens = tokens[:int(len(tokens) * fraction)]

        vocab = set(tokens)

        word2id = {t: i for i, t in enumerate(vocab)}
        id2word = {i: t for i, t in enumerate(vocab)}
        
        return cls(path, raw, tokens, vocab, word2id, id2word)


class HarryPotterDataset(Dataset):
    def __init__(self, hpb: HarryPotterBooks, window: int) -> None:
        super(HarryPotterDataset, self).__init__()
        self.hpb = hpb
        self.window = window

    def __len__(self) -> int:
        return len(self.hpb.tokens) - (self.window + 1)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, int]:
        data = self.hpb.tokens[idx:idx + self.window + 1]
        sentence_tokens, word_token = data[:-1], data[-1]

        sentence = torch.tensor([
            self.hpb.word2id[t] for t in sentence_tokens
        ], dtype=torch.long)
        word = self.hpb.word2id[word_token]
        
        return sentence, word


class JKRowling(nn.Module):
    def __init__(
        self,
        vocab: int,
        embedding: int,
        hidden: int,
        layers: int,
        dropout: float,
    ) -> None:
        super(JKRowling, self).__init__()
        self.embedding = nn.Embedding(vocab, embedding)
        self.lstm = nn.LSTM(
            embedding,
            hidden,
            num_layers=layers,
            dropout=dropout,
            batch_first=True,
        )
        self.fc = nn.Linear(hidden, vocab)

    def forward(self, sentence: torch.Tensor) -> torch.Tensor:
        embedding = self.embedding(sentence) # (B, 50) -> (B, 50, E)
        _, (hn, cn) = self.lstm(embedding)   # (B, 50, E) -> (B, 50, H)
        word = self.fc(hn[-1])               # (B, H) -> (B, V)
        return word


ROOT = "./dataset/full.txt"

NAME = "J"
SURNAME = "JKR"

FRACTION = 0.1
MAX_SEQ = 50    # Do not touch !!!!!!!!

EMBEDDING = 64
HIDDEN = 32
LAYERS = 2
DROPOUT = 0.2

BATCH_SIZE = 256
NUM_WORKERS = 4

EPOCHS = 1
LR = 1e-3
DECAY = 1e-4


hpb = HarryPotterBooks.from_file(ROOT, fraction=FRACTION)
hpd = HarryPotterDataset(hpb, window=MAX_SEQ)

print("===== STATS ====")
print("RAW    :", len(hpb.raw))
print("TOKENS :", len(hpb.tokens))
print("VOCAB  :", len(hpb.vocab))
print("DATASET:", len(hpd))
print("================")
print()

loader = DataLoader(
    hpd,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=NUM_WORKERS,
    pin_memory=True,
)


model = JKRowling(len(hpb.vocab), EMBEDDING, HIDDEN, LAYERS, DROPOUT).cuda()
criterion = nn.CrossEntropyLoss().cuda()

optim = AdamW(model.parameters(), lr=LR, weight_decay=DECAY)


for epoch in range(EPOCHS):
    with tqdm(loader, desc="Train") as pbar:
        total_loss = 0.0
        model = model.train()
        
        for sentence, word in pbar:
            sentence, word = sentence.cuda(), word.cuda()
            optim.zero_grad()

            out = model(sentence)
            loss = criterion(out, word)
            loss.backward()
            optim.step()

            total_loss += loss.item() / len(loader)
            pbar.set_postfix(loss=total_loss)

    with torch.no_grad():
        model = model.eval()

        for idx, i in enumerate([0, 10, 100]):
            sentence_ids, word_id = hpd[i]

            _word_id = model(sentence_ids.unsqueeze(0).cuda())
            _word_id = torch.argmax(_word_id.squeeze(0)).cpu().item()
            
            sentence = [hpb.id2word[i.item()] for i in sentence_ids]
            word = hpb.id2word[word_id]
            _word = hpb.id2word[_word_id]

            print()
            print(f"===== TEST{idx + 1} ====")
            print("SENTENCE  :", " ".join(sentence))
            print("TARGET    :", word)
            print("PREDICTION:", _word)
            print("================")
            print()

torch.jit.script(model.cpu()).save(f"Challenge02_{NAME}_{SURNAME}.ts")
