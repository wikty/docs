import torch
from torch import nn


class NetReLU(nn.Module):

	def __init__(self, sizes):
		super().__init__()
		self.sizes = sizes
		self.linears = torch.nn.ModuleList()
		for in_dim, out_dim in zip(sizes[:-1], sizes[1:]):
			self.linears.append(nn.Linear(in_dim, out_dim))

	def forward(self, x):
		a = x
		for linear in self.linears[:-1]:
			a = linear(a).clamp(min=0.)
		return self.linears[-1](a)


dtype = torch.float
device = torch.device('cpu')
if torch.cuda.is_available():
	device = torch.device('cuda:0')
print('Device: {}'.format(device))

epoch = 5000
train_n = 100
learning_rate = 1e-8
in_dim, hidden_dim, out_dim = 1000, 500, 10
x = torch.randn(train_n, in_dim, dtype=dtype, device=device)
y = torch.randn(train_n, out_dim, dtype=dtype, device=device)

net = NetReLU((in_dim, hidden_dim, hidden_dim, hidden_dim, out_dim)).cuda(device)
loss_fn = nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

# train
for e in range(epoch):
	output = net(x)
	loss = loss_fn(output, y)
	print('Loss: {}'.format(loss.item()))
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()