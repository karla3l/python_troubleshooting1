# Dada uma letra minúscula, qual sua correspondente em maiúsculo?

letra = input("Digite uma letra minuscula: \t")
codigo = ord(letra)

if  97 <= codigo <= 122:
    letra_ma = chr(codigo - 32)
    print(f"A letra em minúsculo é '{letra_ma}'")
else:
    print('Não é uma letra minuscula válida.')