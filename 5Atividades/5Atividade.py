# Dados dois inteiros m e n, gerar três inteiros aleatórios múltiplos de m entre 0 e n

import random

m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

# Garante que m seja menor ou igual a n
if m > n:
    m, n = n, m

# Calcula a quantidade de múltiplos de m no intervalo [0, n]
quantidade_multiplos = n // m

# Gera três inteiros aleatórios múltiplos de m entre 0 e n
aleatorio1 = random.randint(0, quantidade_multiplos) * m
aleatorio2 = random.randint(0, quantidade_multiplos) * m
aleatorio3 = random.randint(0, quantidade_multiplos) * m

# Exibe os inteiros aleatórios gerados
print(f"Três inteiros aleatórios múltiplos de {m} entre 0 e {n}:")
print(aleatorio1)
print(aleatorio2)
print(aleatorio3)
