# Dados tres inteiros x,y e z, quais os inteiros multiplos de z entre x e y inclusivos?
# resolva usando o for

x = int(input("Digite um num"))
y = int(input("Digite um num"))
z = int(input("Digite um num"))
multiplos=[]

for i in range(x,y,1):
    if i % z == 0:
        multiplos.append(i)
print(multiplos)
#_________________________________________________________________________________________

x = int(input("Digite um num"))
y = int(input("Digite um num"))
z = int(input("Digite um num"))

if x > y:
    aux = x
    x=y
    y=aux
for i in range(x,y+1):
    if i % z == 0:
        print(i)