# Atividade 6
# Dados dois números, qual o maior deles e a diferença absoluta entre eles?
# (a diferença absoluta é o maior menos o menor).

num1 = int(input("Digite uma numero: \t"))
num2 = int(input("Digite uma numero: \t"))


if num1 > num2:
    print("Numero 1 é maior", num1)
    print("A diferença absoluta eh: \t", num1-num2)
else:
    print("Numero 2 é maior", num2)
    print("A diferença absoluta eh: \t", num2-num1)