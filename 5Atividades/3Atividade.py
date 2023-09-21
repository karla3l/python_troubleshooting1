# Dado um inteiro n, gerar três inteiros aleatórios entre −n e n

import random

n = int(input("Digite um número inteiro n: "))

# Gera três inteiros aleatórios entre -n e n
aleatorio1 = int(random.random() * (2 * n + 1)) - n
aleatorio2 = int(random.random() * (2 * n + 1)) - n
aleatorio3 = int(random.random() * (2 * n + 1)) - n

# Exibe os inteiros aleatórios gerados
print("Três inteiros aleatórios gerados entre -", n, "e", n, ":")
print(aleatorio1)
print(aleatorio2)
print(aleatorio3)
