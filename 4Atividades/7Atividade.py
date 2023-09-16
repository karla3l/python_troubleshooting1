# Dada uma letra maiúscula, qual sua correspondente em minúsculo?

letra = input("Digite uma letra maiúscula: \t")
codigo = ord(letra)

if 65 <= codigo <= 90:
    letra_min = chr(codigo + 32)
    print(f"A letra em minúsculo é '{letra_min}'")
else:
    print('Não é uma letra maiúscula válida.')

