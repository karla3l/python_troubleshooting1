# Dada uma letra e um inteiro N, qual a letra correspondente ao andar N casas à frente da
# letra lida (ou atrás, se o N for negativo).

letra = input("Digite uma letra: \t")
n = int(input("Digite um inteiro N: \t"))

codigo_letra = ord(letra.upper())  # Converte para maiúscula para garantir consistência

if 65 <= codigo_letra <= 90:
    novo_codigo_letra = codigo_letra + n
    if 65 <= novo_codigo_letra <= 90:
        letra_modificada = chr(novo_codigo_letra)
        print(f"A letra correspondente após andar {n} casa(s) é '{letra_modificada}'.")
    else:
        print("A operação resulta em uma letra fora do alfabeto.")
else:
    print('Por favor, digite uma letra do alfabeto (A-Z).')
