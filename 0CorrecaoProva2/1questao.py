# Dados tres inteiros x,y e z, quais os inteiros multiplos de z entre x e y inclusivos?
# resolva usando o while

x = int(input("Digite um num"))
y = int(input("Digite um num"))
z = int(input("Digite um num"))

if x > y:
    aux = x
    x=y
    y=aux
while x<=y:
    if x%z==0:
        print(x)
    x+=1