# Atividade 5
# Dados dois números, um deles é múltiplo do outro?

n1 = int(input())
n2 = int(input())

if n1 % n2 == 0 or n2 % n1 == 0:
    print("sim")
else:
    print("nao")
    
