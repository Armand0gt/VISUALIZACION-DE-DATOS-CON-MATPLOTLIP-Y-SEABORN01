import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 11)
Y = np.sin(X)

fig, axes = plt.subplots()
axes.plot(X,Y,"b")
fig.show()

fig, axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(X,Y,"r")
axes[1].plot(X,Y,"y")
fig.show()


fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2)
ax1.plot(X,Y,"r")
ax2.plot(X,Y,"y")
fig.show()


fig, axes= plt.subplots(2,4)
axes[0,0].plot(X, np.cos(X),"b")
axes[0,1].plot(X, np.sin(X),"r")
axes[0,2].plot(X, np.tan(X),"y")
axes[0,3].plot(X, np.cos(X)**2)
fig.show()


fig, ((ax1,ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2,4)
ax1.plot(X, np.cos(X),"b")
ax2.plot(X, np.sin(X),"r")
ax3.plot(X, np.tan(X),"y")
ax4.plot(X, np.cos(X)**2)
ax5.plot(X, np.cos(X),"b")
ax6.plot(X, np.sin(X),"r")
ax7.plot(X, np.tan(X),"y")
ax8.plot(X, np.cos(X)**2)
fig.tight_layout()
fig.show()