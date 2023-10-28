# Dado um natural no sistema decimal, qual seu equivalente no sistema binário? Para realizar a conversão do sistema 
# decimal para binário, realiza-se a divisão sucessiva por 2. O resultado da conversão será dado pelo último quociente
# (MSB) e o agrupamento dos restos das divisões.

decimal = int(input("Digite um número decimal: "))
binario = ""
while decimal > 0:
    resto = decimal % 2  # Calcula o resto da divisão por 2
    binario = str(resto) + binario  # Acrescenta o resto à esquerda do resultado binário
    decimal = decimal // 2  # Faz a divisão inteira por 2
print(f"O equivalente binário é: {binario}")
