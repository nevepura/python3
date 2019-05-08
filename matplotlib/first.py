import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(10)]
y = [x[i]**2 for i in range(len(x))]
z =  [x[i]**3 for i in range(len(x))]


plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='cubic')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title("Simple Plot")

plt.legend()

plt.show()

