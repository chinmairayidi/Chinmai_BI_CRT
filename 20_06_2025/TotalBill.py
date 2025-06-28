import numpy as np
prices = np.array([50,50,30])
qualities = np.array([2,2,3])
total = (prices * qualities)
total = total.sum()
print(total)