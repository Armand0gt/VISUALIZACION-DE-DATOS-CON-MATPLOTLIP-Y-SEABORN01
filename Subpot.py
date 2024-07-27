import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,5,11) #Ne crea una lista
Y= X**2
#Dos graficos en una misma imagen
plt.subplot(1,2,1) # Esto crea un área de gráfico con 2 filas y 1 columna, y selecciona la primera posición (la parte superior).
plt.plot(X,Y, "r") #Tipo de grafico, Eje x y y de color Rojo
plt.subplot(1,2,2) #Segunda grafica fila 1, colum 2.
plt.hist(Y)        #Tipo de grafico, Eje x y y de color Rojo    
plt.show()         #Visualizar el grafico. 

#Dos graficos en una misma imagen pero en la imagen 1 con dos lineas
plt.subplot(1,2,1)
plt.plot(X,"r--")
plt.plot(Y,"b--")
plt.subplot(1,2,2)
plt.pie(Y)
plt.show()

#Dos graficos en una misma imagen pero en la imagen 1 con dos lineas e inverso
plt.subplot(2,1,1)
plt.plot(X,"r--")
plt.plot(Y,"b--")
plt.subplot(2,1,2)
plt.pie(Y)
plt.show()


plt.subplot(2,1,1)
plt.plot(X,Y,"r--")
plt.plot(Y, X,"b--")
plt.subplot(2,1,2)
plt.pie(Y)
plt.show()