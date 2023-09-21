# Gerar dois inteiros aleatórios cuja soma esteja entre [0 e 100).

import random

# Gera um inteiro aleatório entre 0 e 99
primeiro_inteiro = int(random.random() * 100)

# Gera o segundo inteiro de forma que a soma esteja entre 0 e 100
segundo_inteiro = int(random.random() * (100 - primeiro_inteiro))

# Exibe os inteiros aleatórios gerados
print(f"Dois inteiros aleatórios cuja soma está entre 0 e 100:")
print(primeiro_inteiro)
print(segundo_inteiro)
#_______________________________________________________________-


# Gera um inteiro aleatório entre 0 e 99
primeiro_inteiro = random.randint(0, 99)

# Gera o segundo inteiro de forma que a subtração esteja entre 0 e 100
segundo_inteiro = random.randint(0, primeiro_inteiro + 100)

# Exibe os inteiros aleatórios gerados e a subtração
print(f"Subtração de {primeiro_inteiro} por {segundo_inteiro} está entre 0 e 100:")
print(f"Resultado da subtração: {primeiro_inteiro - segundo_inteiro}")
#_______________________________________________________________________________


# Gera um inteiro aleatório entre 0 e 9
primeiro_fator = random.randint(0, 9)

# Limita o segundo fator para evitar multiplicação maior ou igual a 100
# Se o primeiro fator for 0, o segundo fator será 0
if primeiro_fator != 0:
    segundo_fator = random.randint(0, 100 // primeiro_fator)
else:
    segundo_fator = 0

# Exibe os inteiros aleatórios gerados e a multiplicação
print(f"Multiplicação de {primeiro_fator} por {segundo_fator} está entre 0 e 100:")
print(f"Resultado da multiplicação: {primeiro_fator * segundo_fator}")
#_______________________________________________________________________________


# Gera o numerador (um inteiro aleatório entre 1 e 99)
numerador = random.randint(1, 99)

# Gera o denominador de forma que a divisão esteja entre 0 e 100
denominador = random.randint(1, numerador * 100)  # Limita para evitar divisão por zero

# Limita o denominador para evitar uma divisão maior ou igual a 100
if denominador > numerador * 100:
    denominador = numerador * 100

# Exibe os inteiros aleatórios gerados e a divisão
print(f"Divisão de {numerador} por {denominador} está entre 0 e 100:")
print(f"Resultado da divisão: {numerador / denominador:.2f}")


