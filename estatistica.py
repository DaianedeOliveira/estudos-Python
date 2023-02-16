import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([1.50, 2.50, 4.0, 5.0])
y= ["Pão", "Detergente", "Iogurte", "Banana"]

plt.subplot(1, 2, 1)
plt.plot(x, y,'o:g', ms= 15)

plt.title("Lista de compras no mercado",
          fontsize = 10,
          color =  "Green",
          fontweight = "bold")

plt.xlabel("Preço", fontsize=10,
           color="Green",
           fontweight="bold")
plt.ylabel("Produtos", fontsize=5,
           color="Green",
           fontweight="bold")
plt.grid(color = "gray", ls = '--', linewidth = 0.2)


#plot 2
x = np.array(["Banana", " Maça", "Manga", "Pera", "Amora", "Ameixa"])
y = np.array([5.0, 6.0, 5.0, 4.5, 8.0, 4.5])
plt.subplot(1,2,2)
plt.plot(x,y, 'o:m')

plt.title("Hortifruti - Lista de compras",
          fontsize = 10,
          color =  "purple",
          fontweight = "bold")


plt.xlabel("Preço", fontsize=10,
           color="purple",
           fontweight="bold")

plt.ylabel("Frutas", fontsize=5,
           color="purple",
           fontweight="bold")
plt.grid(color = "gray", ls = ':', linewidth = 0.2)
plt.show()