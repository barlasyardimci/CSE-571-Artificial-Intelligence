from Data_Loaders import Data_Loaders
from Networks import Action_Conditioned_FF

import torch
import torch.nn as nn
import matplotlib.pyplot as plt


def train_model(no_epochs):

    batch_size = 100
    data_loaders = Data_Loaders(batch_size)
    model = Action_Conditioned_FF()


    losses = []
    loss_function = nn.MSELoss()
    min_loss = model.evaluate(model, data_loaders.test_loader, loss_function)
    losses.append(min_loss)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)


    for epoch_i in range(no_epochs):
        model.train()
        for idx, sample in enumerate(data_loaders.train_loader): # sample['input'] and sample['label']
            inputs, labels = sample['input'], sample['label']
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_function(outputs, labels)
            losses.append(loss.item())
            loss.backward()
            optimizer.step()
            #if idx % 10 == 9:
            print('[%d, %5d] loss: %.3f' % (epoch_i + 1, idx + 1, loss))

    plt.plot(losses)
    plt.ylabel("sample loss")
    plt.show()
    torch.save(model.state_dict(), 'saved/saved_model.pkl',_use_new_zipfile_serialization=False)
    min_loss = model.evaluate(model, data_loaders.test_loader, loss_function)
    print("Min_Loss", min_loss)

if __name__ == '__main__':
    no_epochs = 800
    train_model(no_epochs)
