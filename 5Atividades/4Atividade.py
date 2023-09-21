# Dados dois inteiros m e n, gerar três inteiros aleatórios entre m e n.

import random

m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

# Garante que m seja menor ou igual a n
if m > n:
    m, n = n, m

# Gera três inteiros aleatórios entre m e n
aleatorio1 = random.random(m, n)
aleatorio2 = random.random(m, n)
aleatorio3 = random.random(m, n)

# Exibe os inteiros aleatórios gerados
print(f"Três inteiros aleatórios gerados entre {m} e {n}:")
print(aleatorio1)
print(aleatorio2)
print(aleatorio3)
