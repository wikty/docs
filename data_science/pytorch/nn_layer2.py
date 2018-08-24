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

# init parameters
w1 = torch.randn(hidden_dim, in_dim, dtype=dtype, device=device)
w2 = torch.randn(out_dim, hidden_dim, dtype=dtype, device=device)

for e in range(epoch):
	# forward: hidden layer
	a0 = x.t()
	z1 = w1.mm(a0)
	a1 = z1.clamp(min=0.)  # (hidden_dim, train_n)
	# forward: output layer
	z2 = w2.mm(a1)
	a2 = z2  # (out_dim, train_n)

	# MSE Loss
	loss = (a2 - y.t()).pow(2).sum().item() / train_n
	print('Loss: {}'.format(loss))

	# backward: output layer
	a2_grad = 2 * (a2 - y.t())
	z2_grad = a2_grad.clone()  # (out_dim, train_n)
	w2_grad = z2_grad.mm(a1.t())
	# backward: hidden layer
	a1_grad = w2.t().mm(z2_grad)
	z1_grad = a1_grad.clone()  # (hidden_dim, train_n)
	z1_grad[z1 < 0.] = 0
	w1_grad = z1_grad.mm(a0.t())

	# update parameters
	w1 -= learning_rate * w1_grad
	w2 -= learning_rate * w2_grad