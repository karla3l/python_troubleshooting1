# Ler um número inteiro e escrever um valor aleatório com base nesse número: 
# uma letra maiúscula se o usuário inseriu 1, uma letra minúscula se o usuário inseriu 2
# e um dígito se o usuário inseriu qualquer valor que não seja 1 ou 2.

import random

# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro (1 para letra maiúscula, 2 para letra minúscula): "))

# Verifica o número e gera o valor aleatório correspondente
if numero == 1:
    # Gera uma letra maiúscula aleatória
    valor_aleatorio = chr(random.randint(65, 90))
elif numero == 2:
    # Gera uma letra minúscula aleatória
    valor_aleatorio = chr(random.randint(97, 122))
else:
    # Gera um dígito aleatório
    valor_aleatorio = str(random.randint(0, 9))

# Exibe o valor aleatório gerado
print("Valor aleatório gerado:", valor_aleatorio)
