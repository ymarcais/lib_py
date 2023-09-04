class Statistician:

	# Mean
	def mean(self, x):
		j = 0
		b = 0
		for i in x:
			b += i
			j += 1
		return b/j 

	# Quartil
	def quartil(self, x, p):
		size = len(x)
		if size == 0:
			return None
		i = int((p / 100) * size)
		x = sorted(x)
		res = None
		if size % 2 == 0:
			res = (x[i - 1] + x[i]) / 2
			res = x[i - 1]
			return res 
		
	# Median
	def median(self, x):
		return self.quartil(x, 50)
	
	# Variance
	def var(self, x):
		size = len(x)
		if size == 0:
			return None
		res = 0
		xmean = self.mean(self, x)
		for i in range(size):
			res +=(x[i] - xmean) ** 2
		return res / size

	# Standard deviation
	def std(self, x):
		return self.var(self, x) ** 0.5
	
def main():
	st = Statistician()

if  __name__ == "__main__":
	main()
