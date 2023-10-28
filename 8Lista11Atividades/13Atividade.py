""" Decompor um número em fatores primos ou, fatorá-lo, é escrever este número como uma multiplicação de números primos. 
Os fatores são termos da multiplicação que, neste caso, são números primos. A fatoração é uma técnica usada em muitos
algoritmos de criptografia sem os quais a internet não existiria da forma como a conhecemos. 
A fatoração de um número natural qualquer se dá pela seguinte forma: Divida o número pelo seu menor divisor primo.
O quociente será o novo número. Continue dividindo o número pelo seu menor divisor primo até chegar em 1. 
A multiplicação de todos os divisores dará o valor do número original. 
Exemplo, os fatores primos de 180 são 2⋅2⋅3⋅3⋅5=180:
 """

n = int(input("Digite um número natural: "))
fatores_primos = []

# Encontrar os fatores primos de 2
while n % 2 == 0:
    fatores_primos.append(2)
    n = n // 2

# Encontrar os fatores primos ímparesuuuuuu
for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
        fatores_primos.append(i)
        n = n // i

# Se o número restante após o loop for maior que 1, é um primo
if n > 1:
    fatores_primos.append(n)

if not fatores_primos:
    print("O número é primo.")
else:
    print(f"Fatores primos de {n}: {fatores_primos}")

