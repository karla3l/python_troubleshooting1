# Atividade 8
# Dados três números representando os lados de um triângulo, ele é equilátero,
# isósceles ou escaleno? (como seria esse exercício sem o else, nem o elif...)

# Um triângulo é chamado equilátero quando seus três lados têm medidas iguais
# Um triângulo é chamado isósceles quando têm dois lados iguais e um diferente
# Um triângulo é chamado escaleno quando nenhum de seus lados são iguais

num1 = int(input("Digite um numero: \t"))
num2 = int(input("Digite um numero: \t"))
num3 = int(input("Digite um numero: \t"))

if num1 == num2: 
    if num1 == num3:
     print("equilátero")
if num1 == num2:
    if num1 != num3:
     print("isósceles")
if num1 == num3:
    if num1 != num2:
     print("isósceles")
if num2 == num3:
    if num2 != num1:
     print("isósceles")
if num1 != num2:
    if num1 != num3:
     print("escaleno")