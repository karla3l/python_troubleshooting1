# Dado um inteiro, quantos dígitos ele tem? (dica: vai dividindo por 10)

numero = int(input("Digite um número inteiro: "))

# Inicializa o contador de dígitos
contador_digitos = 0

# Enquanto o número for diferente de zero, divide por 10 e incrementa o contador
while numero != 0:
    numero //= 10  # Divide o número por 10, ignorando a parte decimal
    contador_digitos += 1

print(f"O número tem {contador_digitos} dígitos.")
