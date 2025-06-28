import numpy as np
ratings = np.array([4, 3, 5, 4, 2, 5, 3, 4, 5, 1])
count = np.sum(ratings == 5)
print("Number of Users who gave Rating of 5 are : ",count)