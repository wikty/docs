import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms


class Net(nn.Module):

    def __init__(self):
        super().__init__()
        # in: 3 channels, out: 6 feature maps
        self.conv1 = nn.Conv2d(3, 6, (5, 5))
        # in: 6 feature maps, out: 16 feature maps
        self.conv2 = nn.Conv2d(6, 16, (5, 5))
        # max-pooling size is 2x2
        self.pool = nn.MaxPool2d(2, 2)
        # the last conv layer output 16 feature maps of 5x5 size
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        """`x` is a mini-batch of samples, not a single sample."""
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        # flatten feature maps and keep the batch size/dim
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def load_data(path, batch_size=4):
    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root=path, train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                              shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR10(root=path, train=False,
                                           download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    return trainloader, testloader, classes


if __name__ == '__main__':
    # hyperparameter
    epoch = 2

    # CUDA device
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(device)

    # CNN
    net = Net()
    print(net)
    # transfer neural network to GPU if it is available
    net.to(device)

    # load data
    trainloader, testloader, classes = load_data('./data')

    # Loss: Cross-Entorpy Loss
    criterion = nn.CrossEntropyLoss()
    # Optimizer: SGD with momentum
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # Training
    for eth in range(epoch):
        running_loss = 0.0
        # for-each all of mini-batches in trainset
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            # transfer train data on GPU if it is available
            inputs.to(device)
            labels.to(device)

            # zero the parameter gradients
            optimizer.zero_grad()
            # forward
            outputs = net(inputs)
            # loss
            loss = criterion(outputs, labels)
            # backward
            loss.backward()
            # update parameters
            optimizer.step()

            running_loss += loss.item()
            if (i != 0) and (i % 2000 == 0):
                print('Epoch:{}, Mini-batch: {}, Loss: {}'.format(
                    eth, i, running_loss/2000
                ))
                running_loss = 0.0
    print('Training Done!')

    # Evaluation
    total, correct = [0]*10, [0]*10
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predictions = torch.max(outputs.data, 1)
            c = (labels==predictions).squeeze()
            for label, s in zip(labels, c):
                total[label] += 1
                correct[label] += s.item()
    print('Accuracy of the 10000 test images: %2d %%' % (
        100*torch.sum(correct)/torch.sum(total)))
    for i in range(10):
        print('Accuracy of %10s: %2d %%' % (
            classes[i], 100 * correct[i] / total[i]))

