# Gerar uma senha numéria aleatória entre 0 e 9999. Dar dez chances para o usuário acertar a senha, informando se o chute é maior ou menor que a senha. Quando o usuário acertar a senha ou chutar dez vezes, escrever a quantidade de tentativas e se ele acertou ou não a senha. Utilie break.

import random
# Gerar uma senha numérica aleatória entre 0 e 9999
senha = random.randint(0, 9999)
tentativas = 0
limite_de_tentativas = 10
while tentativas < limite_de_tentativas:
    chute = int(input("Digite um número entre 0 e 9999: "))
    if chute == senha:
        print(f"Você acertou a senha em {tentativas + 1} tentativas!")
        break
    elif chute < senha:
        print("A senha é maior.")
    else:
        print("A senha é menor.")
    tentativas += 1
if tentativas == limite_de_tentativas:
    print(f"Você esgotou suas 10 tentativas. A senha era {senha}.")
#_____________________________________________________________________________

import random
# Gerar uma senha numérica aleatória entre 0 e 9999
senha = random.randint(0, 9999)
tentativas = 0
for _ in range(10):
    chute = int(input("Digite um número entre 0 e 9999: "))
    tentativas += 1
    if chute == senha:
        print(f"Você acertou a senha em {tentativas} tentativa(s)!")
        break
    elif chute < senha:
        print("A senha é maior.")
    else:
        print("A senha é menor.")
if tentativas == 10:
    print(f"Você esgotou suas 10 tentativas. A senha era {senha}.")

