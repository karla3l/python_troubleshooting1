# Atividade 3
# Dados dois inteiros, algum deles é ímpar?

num1 = int(input("Digite um numero: \t"))
num2 = int(input("Digite um numero: \t"))

if num1 % 2 != 0:
    print("Sim")
elif num2 % 2 != 0:
    print("Sim")
else:
    print("Não")