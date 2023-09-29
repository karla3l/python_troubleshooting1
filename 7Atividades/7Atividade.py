# Atividade 7
# Dados dois números, algum deles NÃO é múltiplo de 5?

n1 = int(input())
n2 = int(input())

if n1 % 5 != 0 or n2 % 5 != 0:
    print("sim")
else:
    print("não")