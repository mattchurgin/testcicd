import scipy
import pandas
import numpy

import matplotlib
from matplotlib import pyplot as plt

def fizzbuzz(x):
	if x%15==0:
		return 'fizzbuzz'
	elif x%5==0:
		return 'fizz'
	elif x%3==0:
		return 'buzz'
	else:
		return str(x)
	

if __name__ == '__main__':
	for i in range(100):
		print(str(i), ': ', fizzbuzz(i))
