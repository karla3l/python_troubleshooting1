import random

primeiro = 10
ultimo = 20
quantidade = ultimo - primeiro + 1
sorteado = primeiro + int(random.random() * quantidade)
print(sorteado)