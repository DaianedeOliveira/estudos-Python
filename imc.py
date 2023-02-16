import numpy as np

peso = np.array([int(40), int(50), int(60)])
altura = np.array([float(1.75), float(1.60), float(1.55)])

Imc = peso / altura ** 2
print('O IMC é:', peso[0],'m', 'e', altura[0],'m de altura')
print('O IMC é:', peso[1],'m', 'e', altura[1],'m de altura')
print('O IMC é:', peso[2],'m', 'e', altura[2],'m de altura')
