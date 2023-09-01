# Atividade 5
# Dados três inteiros, a soma deles é ímpar?

num1 = int(input("Digite um numero: \t"))
num2 = int(input("Digite um numero: \t"))

if (num1+num2) % 2 != 0:
    print("Sim")
else:
    print("Não")