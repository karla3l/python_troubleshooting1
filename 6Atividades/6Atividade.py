# Dada uma sequência de números seguida pelo número zero, qual a soma dos números?

soma = 0
#numero = None
numero = int(input("Digite um número (ou 0 para parar): "))

while numero != 0:
    numero = int(input("Digite um número (ou 0 para parar): "))
    soma += numero

print(f"A soma dos números digitados (excluindo 0) é: {soma}")

