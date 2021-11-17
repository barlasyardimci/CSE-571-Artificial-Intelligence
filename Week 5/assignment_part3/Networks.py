import torch
import torch.nn as nn

class Action_Conditioned_FF(nn.Module):
    def __init__(self):
# STUDENTS: __init__() must initiatize nn.Module and define your network's
# custom architecture
        super(Action_Conditioned_FF, self).__init__()
        self.fc1 = nn.Linear(6,32)
        self.fc2 = nn.Linear(32,2)

    def forward(self, input):
# STUDENTS: forward() must complete a single forward pass through your network
# and return the output which should be a tensor
        input = nn.ReLU(self.fc1(input))
        output = nn.Sigmoid(self.fc2(input))
        return output


    def evaluate(self, model, test_loader, loss_function):
# STUDENTS: evaluate() must return the loss (a value, not a tensor) over your testing dataset. Keep in
# mind that we do not need to keep track of any gradients while evaluating the
# model. loss_function will be a PyTorch loss function which takes as argument the model's
# output and the desired output.
        prediction = model(test_loader.dataset)
        loss = loss_function(prediction, test_loader)
        return loss

def main():
    model = Action_Conditioned_FF()

if __name__ == '__main__':
    main()
