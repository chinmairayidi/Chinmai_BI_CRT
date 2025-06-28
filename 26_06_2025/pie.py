# import numpy as np
# import matplotlib.pyplot as plt
# y = np.random.normal([17,15,20])
# plt.pie(y)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
y = np.array([17,35,15,20])
mylabel=["apple","banana","choclate","kivi"]
myexplode =[0,0,0.1,0]
plt.pie(y,labels=mylabel,startangle=180,explode=myexplode,shadow=True)
plt.legend(title ="Four Fruits:")
plt.show()
