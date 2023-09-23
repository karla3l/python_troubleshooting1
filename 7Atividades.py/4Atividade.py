# Atividade 4
# Dado um número, ele é múltiplo de 3 ou 5, mas não simultaneamente pelos dois?
# 15 é multiplo de 3 e de 5, logo a resposta é não
# 18 é multiplo apenas de 3, logo é sim
# 17 não é multiplo de ngm, logo é não

num = int(input())

if num % 3 == 0 or num % 5 == 0:
    print("nao")
elif num % 3 != 0 and num % 5 != 0:
    print("não")
else:
    print("sim")

