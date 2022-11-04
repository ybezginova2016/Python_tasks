import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

title = 'Plot sin()'
filename = 'plot.jpg'

plt.title(title)
plt.savefig(filename)