# Atividade 4
# Dados dois inteiros, ambos são pares?

num1 = int(input("Digite um numero: \t"))
num2 = int(input("Digite um numero: \t"))

if num1 % 2 == 0:
    if num2 % 2 == 0:
     print("Sim")
else:
    print("Não")