# Atividade 6
# Dados três números, todos são múltiplos de 10?

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 % 10 == 0 and  num2 % 10 == 0 and  num3 % 10 == 0:
    print("sim")
else:
    print("não")

