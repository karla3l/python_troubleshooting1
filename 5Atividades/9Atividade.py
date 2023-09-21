# Gerar três decimais aleatórios entre [-100 e 100], com até duas casas decimais.

import random

# Gera três decimais aleatórios entre -100 e 100, com até duas casas decimais
decimal1 = random.random() * 200 - 100
decimal1 = int(decimal1 * 100) / 100

decimal2 = random.random() * 200 - 100
decimal2 = int(decimal2 * 100) / 100

decimal3 = random.random() * 200 - 100
decimal3 = int(decimal3 * 100) / 100

# Exibe os decimais gerados
print(f"Três decimais aleatórios entre -100 e 100: {decimal1}, {decimal2}, {decimal3}")
#___________________________________________________________________________


# Gera três decimais aleatórios entre -1000 e 1000, com até três casas decimais
decimal1 = random.random() * 2000 - 1000
decimal1 = int(decimal1 * 1000) / 1000

decimal2 = random.random() * 2000 - 1000
decimal2 = int(decimal2 * 1000) / 1000

decimal3 = random.random() * 2000 - 1000
decimal3 = int(decimal3 * 1000) / 1000

# Exibe os decimais gerados
print(f"Três decimais aleatórios entre -1000 e 1000: {decimal1}, {decimal2}, {decimal3}")
#____________________________________________________________


# Gera três decimais aleatórios entre -10 e 10, com até uma casa decimal
decimal1 = int(random.random() * 200 - 100) / 10.0
decimal2 = int(random.random() * 200 - 100) / 10.0
decimal3 = int(random.random() * 200 - 100) / 10.0

# Exibe os decimais gerados
print(f"Três decimais aleatórios entre -10 e 10: {decimal1}, {decimal2}, {decimal3}")
