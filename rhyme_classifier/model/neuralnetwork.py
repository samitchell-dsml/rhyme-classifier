'''
Defines a neural network for building our model
'''

from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(1716, 1146),
            nn.ReLU(),
            nn.Linear(1146,1146),
            nn.ReLU(),
            nn.Linear(1146, 2),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)

        return logits
