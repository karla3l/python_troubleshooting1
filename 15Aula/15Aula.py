import random
 
# sorteia um float no intervalo [0,1)
sorteado = random.random()
print(sorteado)
 
# transforma em um float entre [0,10)
sorteado = sorteado * 10
print(sorteado)
 
# descarta a parte decimal
int_sorteado = int(sorteado)
print(int_sorteado)