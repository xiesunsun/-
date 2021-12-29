import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5)
plt.figure('三次图像与二次图像')
y1=x**2
y2=x**3
plt.plot(x,y1)
plt.plot(x,y2,color='red',linestyle='--')
plt.show()