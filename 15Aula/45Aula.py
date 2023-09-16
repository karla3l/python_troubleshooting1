import random

primeiro = 50
ultimo = 100
diferenca = 5
quantidade = (ultimo - primeiro) / diferenca + 1
sorteado = primeiro + diferenca * int(random.random() * quantidade)
print(sorteado)