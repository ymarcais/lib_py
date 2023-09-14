import numpy as np
from dataclasses import dataclass

@dataclass
class GradientDescent:
	thetas: np.ndarray
	alpha: np.ndarray
	max_iter: int

	# add a column full of one and convert to numpy array
	def add_one_column(self, x):
		x = np.asarray(x)
		if isinstance(x, (np.ndarray, pd.DataFrame)) and x.size != 0:
			X = np.column_stack((np.ones(len(x)), x))
			return X
		else:
			print("ERROR: x Numpy Array")
			exit()

	# prediction: y_hat = X * theta
	def ft_y_hat(self, x):
		X = self.add_one_column(x)
		y_hat = np.matmul(X, self.thetas)
		return y_hat

	#ŷ = hθ(x)
	#tmp_theta(0) = (1/m)sum((hθ(x(i) ) − y(i)))
	#tmp_theta(0) = (1/m)sum((hθ(x(i) ) − y(i))) * 1 
	#tmp_theta(0) = (1/m)sum((hθ(x(i) ) − y(i))) * x0(i) // rewrite 1 as x0(i) :
	#tmp_theta(1) = (1/m)sum((hθ(x(i) ) − y(i))) * x1(i)
	#Vectorisation:
		# hθ (x) = X' * θ    // hθ (x) = θ0 + θ1 x
		# tmp_theta(j) = (1 / m) * (X' * θ - y) * X'(j)
		# tmp_theta = (1 / m) * transpose(X') * (X' * θ - y) 
	def simple_gradient(self, x, y):
		m = len(x)
		X = self.add_one_column(x)
		y_hat = self.ft_y_hat(x)
		cost = (y_hat - y)
		gradient = (1/(2 * m)) * np.dot(X.T, cost)
		return gradient

	# gradient descent
	def gradient_descent(self, x, y, thetas, alpha, max_iter, epsilon=1e-3):
		i= 0
		m = len(x)
		prev_cost = 10.0
		alpha = self.alpha
		alpha = np.reshape(alpha, (2, 1))
		while i < max_iter:
			gradient = self.simple_gradient(x, y)
			thetas -= alpha * gradient
			i += 1
			y_hat = self.ft_y_hat(x)
			current_cost = (1 / (2 * m)) * np.sum((y_hat - y)**2)
			if abs(current_cost - prev_cost) < epsilon :
				print("Converged at iteration", i+1)
				break
			alpha *= 0.99999
			prev_cost = current_cost
		return thetas
	
	#Calculate the accuracy of the models
	def my_accuracy(self, X, Y, W, B):
		Z = np.dot(W.T, X) + B
		A = self.sigmoid(Z)
		A = A > 0.5

		A = np.array(A, dtype= 'int64')
		Y = Y.T
		acc = (1 -np.sum(np.absolute(A - Y))/ Y.shape[1])*100
		acc = f"{acc:.2f}"
		print("Accuracy : ", acc, "%")