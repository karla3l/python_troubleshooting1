# Gerar uma letra aleatória entre 'a' e 'z

import random

# Gera um número aleatório entre os códigos ASCII de 'a' e 'z'
codigo_aleatorio = random.randint(ord('a'), ord('z'))

# Converte o código para a letra correspondente
letra_aleatoria = chr(codigo_aleatorio)

# Exibe a letra aleatória gerada
print(f"Letra aleatória entre 'a' e 'z': {letra_aleatoria}")
#___________________________________________________________________________

# Gera três letras aleatórias entre 'a' e 'z'
letra1 = chr(random.randint(ord('a'), ord('z')))
letra2 = chr(random.randint(ord('a'), ord('z')))
letra3 = chr(random.randint(ord('a'), ord('z')))

# Exibe as letras aleatórias geradas
print(f"Três letras aleatórias entre 'a' e 'z': {letra1}, {letra2}, {letra3}")
#_______________________________________________________________________________

# Gera três números inteiros aleatórios entre 0 e 100
numero1 = random.randint(0, 100)
numero2 = random.randint(0, 100)
numero3 = random.randint(0, 100)

# Exibe os números inteiros aleatórios gerados
print(f"Três números inteiros aleatórios entre 0 e 100: {numero1}, {numero2}, {numero3}")

