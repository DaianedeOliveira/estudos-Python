import matplotlib.pyplot as plt

materias_da_escola = ["física", "matemática", "sociologia", "biologia"]
notas_da_escola = [6, 10, 8, 9]
plt.plot(materias_da_escola, notas_da_escola, 'o:g')
plt.title('Notas da escola')
plt.show()
