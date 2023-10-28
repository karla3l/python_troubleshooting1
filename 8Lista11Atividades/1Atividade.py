# Refaça os exemplos da seção Mais exemplos de for usando while em vez de for

# Contando de 1 a 100 em incrementos de 1:
# FOR: 
for i in range(1, 101): print(i)
# WHILE
i = 1
while i <= 100:
    print(i)
    i += 1

# Contando de 100 a 1 em decrementos de 1:
# FOR
for i in range(100, 0, -1): print(i)
# WHILE
i = 100
while i >= 1:
    print(i)
    i -= 1

# Contando de 7 a 77 em incrementos de 7:
# FOR
for i in range(7, 78, 7): print(i)
# WHILE
i = 7
while i <= 77:
    print(i)
    i += 7

# Contando de 20 a 2 em decrementos de 2:
# FOR
for i in range(20, 1, -2): print(i)
# WHILE 
i = 20
while i >= 2:
    print(i)
    i -= 2

# Incrementando entre os valores 2, 5, 8, 11, 14, 17, 20:
# FOR
for i in range(2, 21, 3): print(i)
# WHILE
i = 2
while i <= 20:
    print(i)
    i += 3

# Decrementando entre os valores 99, 88, 77, 66, 55, 44, 33, 22, 11, 0:
# FOR
for i in range(99, -1, -11): print(i)
# WHILE
i = 99
while i >= 0:
    print(i)
    i -= 11
