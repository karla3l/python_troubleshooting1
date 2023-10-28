# Dado um inteiro, quantos digitos ele tem? (dica: vai dividindo por dez até chegar no zero)

n = int(input())
cont = 0

while n!=0:
    cont+=1
    n//=10

print(cont)
