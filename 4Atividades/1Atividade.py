# Dado um caractere, qual o seu valor na tabela ASCII?
caractere = input("Digite um caractere: \t")
valor = ord(caractere)
print(f"O valor ASCII de '{caractere}' é {valor}")


# Dado um valor, qual o seu caractere na tabela ASCII?
valor = int(input("Digite um valor na tabela ASCII: "))
caractere = chr(valor)
print(f"O caractere correspondente ao valor {valor} na tabela ASCII é '{caractere}'")
