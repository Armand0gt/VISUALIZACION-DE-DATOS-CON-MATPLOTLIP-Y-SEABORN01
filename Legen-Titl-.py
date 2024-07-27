import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 11)
Y = np.sin(X)

fig, axes = plt.subplots(1,2, figsize = (10,10))
axes[0].plot(X,Y, label="sin(x)")
axes[0].set_title("Relación X - Y")
axes[0].set_ylabel("Y")
axes[0].set_xlabel("X")
axes[0].legend()
axes[1].plot(Y,X, label = "sin(y)")
axes[1].set_title("Relación Y - X")
axes[1].set_ylabel("Y")
axes[1].set_xlabel("X")
axes[1].legend()
fig.show()


#Otra forma
plt.plot(X,Y, label = "sin(x)")
plt.title("Este sera el titulo")
plt.xlabel("Eje x")
plt.ylabel("Eje Y")
plt.legend(loc = "lower left")
plt.show()
