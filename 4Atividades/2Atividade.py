# Dado um caractere, ele é uma letra?

caractere = input("Digite um caractere: \t")

if ('a' <= caractere <= 'z') or ('A' <= caractere <= 'Z'):
    print('Eh uma letra')
else:
    print('Não eh uma letra')