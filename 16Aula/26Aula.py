i = 1
soma = 0
while i < 5:
    print("+", i, end=' ')
    soma = soma + i
    i = i + 1
print("=", soma)

bit = 512
p = 0
while bit > 1:
    print(bit)
    p = p + 1
    bit = bit // 2
print("=", p)