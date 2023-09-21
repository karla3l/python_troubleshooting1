# Dado um natural n, qual a soma dos pares entre 1 e n?

n = int(input("Digite um número natural (n): "))
# Verifica se n é ímpar e ajusta para o número anterior (par)
if n % 2 != 0:
    n -= 1
# A fórmula da soma dos pares é n * (n + 2) / 4
soma = (n * (n + 2)) // 4
print(f"A soma dos números pares entre 1 e {n} é: {soma}")
#___________________________________________________________

# Dado um natural n, qual a soma dos impares entre 1 e n?
n = int(input("Digite um número natural (n): "))

# Calcula a soma dos ímpares usando a fórmula
soma_impares = ((n + 1) // 2) ** 2
print(f"A soma dos números ímpares entre 1 e {n} é: {soma_impares}")


