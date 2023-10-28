# Dado um natural menor que 10000, qual sua forma por extenso? Por exemplo, dado o número 9243, sua forma por extenso é "nove mil duzentos e quarenta e três".

def numero_por_extenso(n):
    if n < 0 or n >= 10000:
        return "Número fora do intervalo válido."
    if n == 0:
        return "zero"

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    milhares = n // 1000
    centenas = (n % 1000) // 100
    dezenas = (n % 100) // 10
    unidades = n % 10

    por_extenso = ""

    if milhares > 0:
        por_extenso += unidades[milhares]
        if milhares > 1:
            por_extenso += " mil"

    if centenas > 0:
        if milhares > 0:
            por_extenso += " e "
        por_extenso += centenas[centenas]
        if dezenas > 0 or unidades > 0:
            por_extenso += " e "

    if dezenas > 1:
        por_extenso += dezenas[dezenas]
        if unidades > 0:
            por_extenso += " e "/8
    elif dezenas == 1:
        if unidades > 0:
            por_extenso += dezenas[dezenas + 10]
        else:
            por_extenso += dezenas[dezenas]
    if unidades > 0:
        por_extenso += unidades[unidades]

    return por_extenso

numero = int(input("Digite um número (menor que 10000): "))
extenso = numero_por_extenso(numero)
print(f"Em extenso: {extenso}")
