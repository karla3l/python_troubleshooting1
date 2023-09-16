# Dadas duas letras, quantas letras há entre as duas?

letra1 = input("Digite a primeira letra: \t")
letra2 = input("Digite a segunda letra: \t")

codigo1 = ord(letra1.upper())  # Converte para maiúscula parta garantir consistência
codigo2 = ord(letra2.upper())  # Converte para maiúscula para garantir consistência

if 65 <= codigo1 <= 90 and 65 <= codigo2 <= 90:
    diferenca = abs(codigo2 - codigo1) - 1  # Calcula a diferença entre os códigos ASCII
    print(f"Há {diferenca} letra(s) entre '{letra1}' e '{letra2}'.")
else:
    print('Por favor, digite letras do alfabeto (A-Z).')
