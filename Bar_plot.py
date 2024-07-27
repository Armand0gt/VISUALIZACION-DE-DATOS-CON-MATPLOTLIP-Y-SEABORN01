import numpy as np
import matplotlib.pyplot as plt

#GBarra
Crop = ["Tomato", "Pepper","Pineapple", "Apple", "Watermelon", "Kiwi"]
Yield = [40, 55, 30, 70, 100, 35]



plt.bar(Crop,Yield, width= 0.8, color = ['red', 'blue', 'green'])
plt.xticks(np.arange(6), ("Tomate", "Chile", "Piña", "Manzana", "Melón", "Kiwi"), rotation = 45)
plt.title("Rendimiento por cultivo")
plt.ylabel("Yield")
plt.xlabel("Crop")
plt.legend(["Yield"])
plt.barh(Crop, Yield)
plt.show ()

#Histrograma
plt.figure(figsize=(10,5))
plt.hist(Yield, bins=6, color = "skyblue", edgecolor = "black")
plt.title("Distribucion del rendimiento")
plt.xlabel("Yield")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show


#Otro histograma
data = np.random.randint(1,50,100)
plt.hist(data, bins=6, histtype = "step")
plt.show()

#Boxplot
data = np.append(data, 200) #Ejemplo de dato atipico
plt.boxplot(data, vert= False, patch_artist= True, notch= True, showfliers=True)
plt.show()

data = np.append(data, 200) #Ejemplo de dato atipico
plt.boxplot(data, vert= False, patch_artist= True, notch= True, showfliers=False) #No muestra los datos atipicos
plt.show()

#Scateer (Grafico de dispersion)
N = 50
X = np.random.rand(N)
Y = np.random.rand(N)
area = (30*np.random.rand(N))**2
colors = np.random.rand(N)
plt.scatter(X, Y, s=area, marker= "p",c=colors, alpha=0.2)
plt.show()
