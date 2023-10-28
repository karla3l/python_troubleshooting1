# Dada uma sequência de 10 inteiros, qual a soma dos múltiplos de 3 e a soma dos múltiplos de 2? Entretanto, múltiplos de 6 não devem ser contabilizados na soma. Utilize continue.

soma_multiplos_3 = 0
soma_multiplos_2 = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))

    if numero % 6 == 0:
        continue  # Pular múltiplos de 6

    if numero % 3 == 0:
        soma_multiplos_3 += numero

    if numero % 2 == 0:
        soma_multiplos_2 += numero

print(f"Soma dos múltiplos de 3: {soma_multiplos_3}")
print(f"Soma dos múltiplos de 2: {soma_multiplos_2}")
