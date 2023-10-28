# Dado um inteiro, qual o seu reverso? Exemplo de entrada→saída: 5837→7385.

num = int(input())
inv = 0

while num != 0:
    resto = num % 10
    inv = inv * 10 + resto

    num = num // 10
print(inv)