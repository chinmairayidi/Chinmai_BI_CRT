import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320])
color = np.array([0, 20, 60, 20, 20, 90, 20, 10, 20])
plt.scatter(x,y,c = color ,cmap='viridis')
plt.show()
