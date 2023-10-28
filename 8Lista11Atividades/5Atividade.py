# Dado um natural, quais seus divisores? Por exemplo, os divisores de 90 são 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90.

num = int(input("Digite um número natural: "))
divisores = []

for i in range(1, num + 1):
    if num % i == 0:
        divisores += [i]
print(f"Os divisores de {num} são: {divisores}")

