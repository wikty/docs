import numpy as np

def sigmoid(z):
	return 1 / (1 + np.exp(-z))

def sigmoid_grad(z):
	return sigmoid(z) * (1 - sigmoid(z))

def identity(z):
	return z

def identity_grad(z):
	return 1

class IdentityActivation(object):

	def fn(self, z):
		return z

	def grad(self, z):
		return 1


class SigmoidActivation(object):

	def fn(self, z):
		return 1 / (1 + np.exp(-z))

	def grad(self, z):
		return self.fn(z) * (1 - self.fn(z))


class MSELoss(object):

	def __init__(self):
		pass

	def fn(self, outputs, targets):
		"""Return the MSE loss of a batch, each row is a sample."""
		return np.sum(np.square(outputs - targets)) / outputs.shape[0]

	def grad(self, outputs, targets):
		return (outputs - targets)


class Net(object):

	def __init__(self, input_size, hidden_size, output_size):
		self.in_size = input_size
		self.h_size = hidden_size
		self.out_size = output_size
		
		## Forward: a0 -> z1 -> a1 -> z2 -> a2
		## Layer-1
		# a0 is input
		self.a0 = None
		# column vector
		self.b1 = np.random.randn(self.h_size, 1)
		# each row of weights is used to activate a hidden unit
		self.w1 = np.random.randn(self.h_size, self.in_size)
		# z1 = dot(w1, a0) + b1
		self.z1 = None
		# a1 = activate(z1)
		self.a1 = None
		self.layer1_act = SigmoidActivation()

		## Layer-2
		self.b2 = np.random.randn(self.out_size, 1)
		self.w2 = np.random.randn(self.out_size, self.h_size)
		# z2 = dot(w2, a1) + b2
		self.z2 = None
		# a2 = activate(z2), a2 is output
		self.a2 = None
		self.layer2_act = IdentityActivation()

		# gradients of the network parameters
		self.b1_grad = np.zeros_like(self.b1)
		self.w1_grad = np.zeros_like(self.w1)
		self.b2_grad = np.zeros_like(self.b2)
		self.w2_grad = np.zeros_like(self.w2)

	def update(self, eta):
		"""Update network's parameters, `eta` is learning rate."""
		self.b1 = self.b1 - eta * self.b1_grad
		self.w1 = self.w1 - eta * self.w1_grad
		self.b2 = self.b2 - eta * self.b2_grad
		self.w2 = self.w2 - eta * self.w2_grad

	def forward(self, x):
		"""`x` is a mini-batch of samples, each row is a sample."""
		self.a0 = x.T
		self.z1 = np.dot(self.w1, self.a0) + self.b1
		self.a1 = self.layer1_act.fn(self.z1)
		self.z2 = np.dot(self.w2, self.a1) + self.b2
		self.a2 = self.layer2_act.fn(self.z2)
		return self.a2.T

	def backward(self, gradients):
		"""`gradients` is a mini-batch gradients for output units, each row
		is for a sample's grandient."""
		batch_size = gradients.shape[0]
		a2_grad = gradients.T
		z2_grad = a2_grad * self.layer2_act.grad(self.z2)
		self.b2_grad = (np.sum(z2_grad, axis=0) / batch_size)
		self.w2_grad = np.dot(z2_grad, self.a1.T) / batch_size
		a1_grad = np.dot(self.w2.T, z2_grad)
		z1_grad = a1_grad * self.layer1_act.grad(self.z1)
		self.b1_grad = (np.sum(z1_grad, axis=0) / batch_size)
		self.w1_grad = np.dot(z1_grad, self.a0.T) / batch_size

if __name__ == '__main__':

	# generate dataset
	epoch = 1
	batch_size = 15
	learning_rate = 0.5
	in_dim, out_dim = 100, 10
	train_n, test_n = 500, int(500/10)
	train_x = np.random.randn(train_n, in_dim)
	train_y = np.random.randn(train_n, out_dim)
	test_x = np.random.randn(test_n, in_dim)
	test_y = np.random.randn(test_n, out_dim)

	# train
	net = Net(in_dim, 50, out_dim)
	loss = MSELoss()
	for e in range(epoch):
		dataset = np.hstack((train_x.copy(), train_y.copy()))
		np.random.shuffle(dataset)
		for i in range(0, train_n, batch_size):
			batch_x = dataset[i:i+batch_size, :in_dim]
			batch_y = dataset[i:i+batch_size, in_dim:]

			outputs = net.forward(batch_x)
			gradients = loss.grad(outputs, batch_y)
			net.backward(gradients)
			net.update(learning_rate)

			score = loss.fn(outputs, batch_y)
			print('{}, {}|{}'.format(e, int(i/batch_size), score))
