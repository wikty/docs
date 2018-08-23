import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Net(nn.Module):

	def __init__(self):
		super().__init__()
		# input image is 1-channels
		self.conv1 = nn.Conv2d(1, 6, (5, 5))
		self.conv2 = nn.Conv2d(6, 16, (5, 5))
		# the last convolution layer output 16 feature maps of 5x5 size
		self.fc1 = nn.Linear(16*5*5, 120)
		self.fc2 = nn.Linear(120, 84)
		self.fc3 = nn.Linear(84, 10)

	def forward(self, x):
		"""`x` is a mini-batch of samples, not a single sample."""
		x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
		x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
		x = x.view(x.size()[0], -1) # flatten feature maps
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x