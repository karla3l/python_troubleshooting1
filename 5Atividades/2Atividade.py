# Dado um inteiro n, gerar três inteiros aleatórios entre 0 e n.

import random

n = int(input("Digite um número inteiro n: "))

# Gera três inteiros aleatórios entre 0 e n
aleatorio1 = int(random.random() * (n + 1))
aleatorio2 = int(random.random() * (n + 1))
aleatorio3 = int(random.random() * (n + 1))

# Exibe os inteiros aleatórios gerados
print("Três inteiros aleatórios gerados entre 0 e", n, ":")
print(aleatorio1)
print(aleatorio2)
print(aleatorio3)
