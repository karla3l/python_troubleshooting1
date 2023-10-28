# Dada uma sequência de inteiros, que termina com 10 números ou com um múltiplo de 6. Qual a soma dos múltiplos de 3 e a soma dos múltiplos de 2? O múltiplo de 6 deve ser contabilizado na soma. Utilize break.

soma_multiplos_3 = 0
soma_multiplos_2 = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (0 para encerrar): "))
    
    if numero == 0:
        break  # Encerra o loop quando 0 é inserido
    
    if numero % 3 == 0:
        soma_multiplos_3 += numero

    if numero % 2 == 0:
        soma_multiplos_2 += numero

    contador += 1

    if contador == 10 or numero % 6 == 0:
        break  # Encerra o loop após 10 números ou ao encontrar um múltiplo de 6

print(f"Soma dos múltiplos de 3: {soma_multiplos_3}")
print(f"Soma dos múltiplos de 2: {soma_multiplos_2}")
