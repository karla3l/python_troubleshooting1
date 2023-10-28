# Dado um natural, qual seu fatorial?

n = int(input("Digite um número natural: "))
fatorial = 1

if n < 0:
    print("O fatorial de um número negativo não é definido.")
elif n == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}.")
