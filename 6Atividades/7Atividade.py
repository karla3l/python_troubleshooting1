# Dada uma sequência de números que termina quando sua soma ultrapassar 1000, qual o maior número?

maior_numero = float('-inf')
soma = 0

while soma <= 1000:
    numero = float(input("Digite um número: "))

    if numero > maior_numero:
        maior_numero = numero

    soma += numero

print(f"O maior número na sequência é: {maior_numero}")
#________________________________________________________________

menor_numero = float('inf')  # Inicializa com infinito, assim qualquer número será menor
soma = 0

while soma <= 1000:
    numero = float(input("Digite um número: "))

    if numero < menor_numero:
        menor_numero = numero

    soma += numero

print(f"O menor número na sequência é: {menor_numero}")

