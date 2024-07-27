import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 11)
Y = X**2

plt.plot(X, Y)
plt.show()

plt.plot(X, Y,"rx")
plt.show()

plt.plot(X, Y,"rs-")
plt.show()

plt.plot(X, Y,"yD:")
plt.show()

plt.hist(X)
plt.show()

plt.pie(X)
plt.show()

plt.scatter(X,Y)
plt.show()

plt.boxplot(X)
plt.show()