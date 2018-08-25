from collections import OrderedDict


import torch


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

# Define Network
# nn.Sequential is a Module which contains other Modules, and applies them in
# sequence to produce the output.
net = torch.nn.Sequential(OrderedDict([
	('linear1', torch.nn.Linear(in_dim, hidden_dim)),
	('relu1', torch.nn.ReLU()),
	('linear2', torch.nn.Linear(hidden_dim, out_dim))
]))
# net = torch.nn.Sequential(
# 	torch.nn.Linear(in_dim, hidden_dim),
# 	torch.nn.ReLU(),
# 	torch.nn.Linear(hidden_dim, out_dim)
# )
net.cuda(device)

# Loss
loss_fn = torch.nn.MSELoss(reduction='sum')

# Train
for e in range(epoch):
	output = net(x)
	loss = loss_fn(output, y)
	print('Loss: {}'.format(loss.item()))
	net.zero_grad()
	loss.backward()

	with torch.no_grad():
		for parameter in net.parameters():
			parameter -= learning_rate * parameter.grad