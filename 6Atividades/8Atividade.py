# Dada uma sequência de inteiros seguida por um múltiplo de 6, qual a soma dos múltiplos 
# de 3 e a soma dos múltiplos de 2? Múltiplos de 6 não devem ser contabilizados na soma. 
# Exemplo: Dada a sequência 5 3 9 11 14 7 4 12, as somas dos múltiplos de 3 e 2 respectivamente são 12 e 18.

print("Digite uma sequencia de numeros. \nDigite um multiplo de 6 para encerrar.")

soma2=0
soma3=0
num = int(input()) #Digite um numero

while num % 6 != 0:
    if num % 2 == 0:
        soma2 += num
    if num % 3 == 0:
        soma3 += num
    num = int(input())
    
print (" A soma dos multiplos de 2 é: \t", soma2)
print (" A soma dos multiplos de 3 é: \t", soma3)