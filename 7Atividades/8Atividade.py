# Atividade 8
# Dados três números, todos são múltiplos de 5 ou de 3?

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 % 5 == 0 or num1 % 3 == 0 and num2 % 5 == 0 or num2 % 3 == 0 and num3 % 5 == 0 or num3 % 3 == 0:
    print("sim")
else:
    print("não")

