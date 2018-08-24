import numpy as np


epoch = 5000
train_n = 100
learning_rate = 1e-8
in_dim, hidden_dim, out_dim = 1000, 500, 10
x = np.random.randn(train_n, in_dim)
y = np.random.randn(train_n, out_dim)

w1 = np.random.randn(hidden_dim, in_dim)
w2 = np.random.randn(out_dim, hidden_dim)

for e in range(epoch):
	# hidden layer forward
	a0 = x.T
	z1 = np.dot(w1, a0)  # shape is (hidden_dim, train_n)
	a1 = np.maximum(z1, 0.)  # ReLU activation
	
	# output layer forward
	z2 = np.dot(w2, a1)  # shape is (out_dim, train_n)
	a2 = z2  # Identity activation

	# MSE Loss of train data
	loss = np.sum(np.square(a2 - y.T)) / train_n
	print('Loss: {}'.format(loss))
	
	# output layer backward
	a2_grad = 2 * (a2 - y.T)  # square error's gradient
	z2_grad = a2_grad.copy()  # (out_dim, train_n)
	w2_grad = np.dot(z2_grad, a1.T)
	
	# hidden layer backward
	a1_grad = np.dot(w2.T, z2_grad)
	z1_grad = a1_grad.copy()
	z1_grad[z1 < 0.] = 0
	w1_grad = np.dot(z1_grad, x)

	# update parameters
	w1 -= learning_rate * w1_grad
	w2 -= learning_rate * w2_grad
