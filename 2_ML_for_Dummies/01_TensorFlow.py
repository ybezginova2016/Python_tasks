# How to use the TensorFlow framework to work through a problem?
#
# For this example, you start with a very simple bidimensional problem inspired by
# the TensorFlow Neural Network Playground (you can find the playground website
# at this address: http://playground.tensorflow.org), trying to divide two
# clouds of points shaped as opposing half-moons positioned in a Cartesian plane:

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
np.random.seed(0)
coord, cl = make_moons(500, noise=0.05)
X, Xt, y, yt = train_test_split(coord, cl, test_size=0.30, random_state=0)
cmap_set1 = plt.cm.Set1

fig, ax = plt.subplots(dpi=90)
ax.scatter(X[:,0], X[:,1], s=25, c=y, cmap=cmap_set1)
plt.show()

# Looking at Figure 14-8, you can see that the task requires formulating a nonlinear
# separation because no straight line can separate the two clouds of points exactly.