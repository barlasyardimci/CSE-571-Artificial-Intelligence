import numpy as np

import torch
import torch.nn as nn

class Action_Conditioned_FF(nn.Module):
    def __init__(self):
# STUDENTS: __init__() must initiatize nn.Module and define your network's
# custom architecture
        super(Action_Conditioned_FF, self).__init__()
        self.fc1 = nn.Linear(6, 256)
        self.fc2 = nn.Linear(256, 1)
        self.ReLU = nn.ReLU()
        self.Sigmoid = nn.Sigmoid()

    def forward(self, input):
# STUDENTS: forward() must complete a single forward pass through your network
# and return the output which should be a tensor
        input = self.ReLU(self.fc1(input))
        output = torch.flatten(self.Sigmoid(self.fc2(input)))
        return output


    def evaluate(self, model, test_loader, loss_function):
# STUDENTS: evaluate() must return the loss (a value, not a tensor) over your testing dataset. Keep in
# mind that we do not need to keep track of any gradients while evaluating the
# model. loss_function will be a PyTorch loss function which takes as argument the model's
# output and the desired output.
        loss = 0.0
        len = 0
        for idx, sample in enumerate(test_loader):
            inputs, labels = sample['input'], sample['label']
            prediction = model(inputs)
            loss += loss_function(prediction, labels).item()
            len += 1
        return loss/len

def main():
    model = Action_Conditioned_FF()

if __name__ == '__main__':
    main()
