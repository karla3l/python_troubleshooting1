# Dado um inteiro n e um dígito d, quantas vezes d ocorre em n? Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

num = int(input("Digite um número inteiro: "))
digito = int(input("Digite um dígito: "))

# Converte o número para uma string
num_str = str(num)

# Inicializa um contador para contar ocorrências do dígito
contador = 0

# Percorre cada dígito na string
for d in num_str:
    if int(d) == digito:
        contador += 1

print(f"O dígito {digito} ocorre {contador} vezes em {num}.")
