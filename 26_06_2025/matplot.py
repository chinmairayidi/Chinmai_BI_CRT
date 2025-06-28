# import numpy as np
# import matplotlib as math
# import matplotlib.pyplot as plt
# print(math.__version__)
# print(math.__version_info__)

# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,'*:g' ,ms=25,mec ='black',mfc='y')
# plt.plot(ypoints,linewidth=55)
# plt.title("sports watch",loc = 'center')  #loc for position
# # plt.xlabel=("calories")
# plt.show()

#linestyles
# 'solid'   '-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'	'' or ' '

#ms=marker size
#mec = marker edge colour 
#mfc =marker face colour
#linewidth
#loc -left,center,right
#label-xlabel,ylabel


# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([80,85,95,100,105,110,115,120,125])
# y=np.array([240,250,260,270,280,290,300,310,320])
# plt.title("sports watch data",loc="center")
# plt.xlabel("average pulse")
# plt.ylabel("calorie burnage")
# plt.plot(x,y)
# plt.grid(axis ='x',color='green',linestyle=':')             #for grid costimisation
# plt.show()




import numpy as np
import matplotlib.pyplot as plt

# First plot
x = np.array([80, 85, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320])
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Plot 1")

x = np.array([80, 85, 95, 100, 105])
y = np.array([240, 250, 260, 270, 233])
plt.subplot(2 ,3 , 2)
plt.plot(x, y)
plt.title("Plot 2")

plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("Plot 3")

plt.subplot(2, 3, 4)
plt.plot(x, y)
plt.title("Plot 4")

plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("Plot 5")

plt.subplot(2, 3, 6)
plt.plot(x, y)
plt.title("Plot 6")
plt.suptitle("xcghjkl")
plt.tight_layout()
plt.show()