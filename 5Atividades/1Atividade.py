# Dado um inteiro como semente, gerar três inteiros aleatórios. 

import random

semente = int(input("Digite a semente para a geração aleatória: "))

# Inicializa a semente para a geração aleatória
random.seed(semente)

# Gera três inteiros aleatórios entre 1 e 100
aleatorio1 = int(random.random() * 100) + 1
aleatorio2 = int(random.random() * 100) + 1
aleatorio3 = int(random.random() * 100) + 1

# Exibe os inteiros aleatórios gerados
print("Três inteiros aleatórios gerados:")
print(aleatorio1)
print(aleatorio2)
print(aleatorio3)
