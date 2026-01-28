import torch
import torch.nn as nn

class VSRModel(nn.Module):
    def __init__(self):
        super(VSRModel, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(3, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.lstm = nn.LSTM(32, 64, batch_first=True)
        self.fc = nn.Linear(64, 30)

    def forward(self, x):
        return self.fc(x)
