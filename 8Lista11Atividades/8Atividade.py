# Dada uma sequência de inteiros seguida por um múltiplo de 11, 13 ou 17, qual o menor número?

menor_numero = float('inf')  # Inicializa com um valor infinito
while True:
    numero = int(input("Digite um número (ou um múltiplo de 11, 13 ou 17 para encerrar): "))  
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        break  # Encerra o loop se o número for múltiplo de 11, 13 ou 17
    if numero < menor_numero:
        menor_numero = numero
if menor_numero == float('inf'):
    print("Nenhum número foi fornecido.")
else:
    print(f"O menor número é: {menor_numero}")
#_____________________________________________________________________________________________

menor_numero = float('inf')  # Inicializa com um valor infinito
for _ in range(1000):  # Assumindo que você não deseja que o loop seja infinito
    numero = int(input("Digite um número (ou um múltiplo de 11, 13 ou 17 para encerrar): "))
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        break  # Encerra o loop se o número for múltiplo de 11, 13 ou 17
    if numero < menor_numero:
        menor_numero = numero
if menor_numero == float('inf'):
    print("Nenhum número foi fornecido.")
else:
    print(f"O menor número é: {menor_numero}")
#_____________________________________________________________________________________________

maior_numero = float('-inf')  # Inicializa com um valor infinitamente pequeno
menor_numero = float('inf')  # Inicializa com um valor infinitamente grande

for _ in range(1000):  # Assumindo que você não deseja que o loop seja infinito
    numero = int(input("Digite um número (ou um múltiplo de 11, 13 ou 17 para encerrar): "))
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        break  # Encerra o loop se o número for múltiplo de 11, 13 ou 17
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

if maior_numero == float('-inf') and menor_numero == float('inf'):
    print("Nenhum número foi fornecido.")
else:
    if maior_numero != float('-inf'):
        print(f"O maior número é: {maior_numero}")
    if menor_numero != float('inf'):
        print(f"O menor número é: {menor_numero}")

