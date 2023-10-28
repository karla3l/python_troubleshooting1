x = int(input("Digite um num"))
y = int(input("Digite um num"))
z = int(input("Digite um num"))
multiplos=[]
if x > y:
    aux = x
    x=y
    y=aux
for i in range(x,y,1):
    if i % z == 0:
        multiplos.append(i)
print(multiplos)
     
