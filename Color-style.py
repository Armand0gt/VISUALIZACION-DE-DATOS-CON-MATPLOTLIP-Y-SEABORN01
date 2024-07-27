import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 11)

print(plt.style.available)
plt.style.use('bmh')

fig , ax = plt.subplots(figsize = (8,8))
ax.plot(X,X+1,"r")
ax.plot(X,X+2,"y")
ax.plot(X,X+3,"p")
ax.plot(X,X+4,"g")
ax.plot(X,X+5,"b")

plt.show()

#Modificaciones de tipo matlab

fig , ax = plt.subplots(figsize = (8,8))
ax.plot(X,X+1,"r--")
ax.plot(X,X+2,"y-")
ax.plot(X,X+3,"b.-")
ax.plot(X,X+4,"go:")
ax.plot(X,X+5,"b")

plt.show()


#Modificaciones de tipo pyplo

fig , ax = plt.subplots(figsize = (8,8))
ax.plot(X,X+1, color = "green", linewidth =2, linestyle = "-", marker = "o", markersize = 20, markerfacecolor = "red")
ax.plot(X,X+2, color = "blue", linewidth =3, linestyle = "--", marker = "x")
ax.plot(X,X+3, color = "#66FF66", alpha = 1, linewidth =4, linestyle = "dashed", marker ="o")
ax.plot(X,X+4, color = "#CCFFCC", linewidth =5, linestyle = "-" , marker = "*")
ax.plot(X,X+5, color = "yellow", linewidth =6, linestyle = "--", marker = "y")

plt.show()
