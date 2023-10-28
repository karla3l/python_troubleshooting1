# Dados dois números inteiros, multiplicá-los usando somas repetidas. Não pode usar o operador de multiplicação "*". 
# Sugestão: usar um laço e o operador de soma (+).

num1 = int(input())
num2 = int(input())
soma = 0

for i in range(num2):
    soma += num1
print(soma)