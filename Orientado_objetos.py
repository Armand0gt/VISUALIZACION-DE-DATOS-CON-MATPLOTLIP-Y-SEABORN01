import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,5,11)
Y = X**2
 
Fig = plt.figure()
Graf = Fig.add_axes([0.1,0.1,0.5,0.9])
Graf.plot(X,Y,"b")
plt.show()


Fig = plt.figure()
Graf = Fig.add_axes([0.1,0.1,0.8,0.9])
Graf2 = Fig.add_axes([0.2,0.55,0.4,0.3])
Graf.plot(X,Y,"b")
Graf2.plot(Y,X,"r")
Graf2.set_facecolor("green")
Fig.show()

