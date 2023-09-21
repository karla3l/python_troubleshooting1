# Dado um natural, ele é primo?

numero = int(input("Digite um número natural: "))

eh_primo = 1  # Assumimos que é primo até provar o contrário (usamos 1 para representar verdadeiro)

# Um número menor que 2 não é primo
if numero < 2:
    eh_primo = 0  # Usamos 0 para representar falso
else:
    # Verifica se o número é divisível por algum número de 2 até a raiz quadrada do número
    divisor = 2
    while divisor * divisor <= numero and eh_primo:
        if numero % divisor == 0:
            eh_primo = 0  # Usamos 0 para representar falso
        divisor += 1

# Exibimos o resultado
if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
