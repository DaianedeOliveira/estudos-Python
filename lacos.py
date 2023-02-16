from numpy import random
import numpy as np

numero_aleatorio = input("Escreva um número aleatório: ")

for i in numero_aleatorio:
    x = random.randint(100, size=(5))
    print(x)

#dicionario
    teste_lista = {
        'nome': 'Daiane',
        'idade': 18,
        'país': 'Brasil'
    }
    print(teste_lista['nome'])


    #vstack
    arr1 = np.array([1,2,3,4,5])
    arr2 = np.array([10,15,20,25, 30])
    arr = np.vstack((arr1, arr2))
    print(arr)