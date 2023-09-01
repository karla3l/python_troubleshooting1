# Dados dois inteiros m e n, qual o maior multiplo de m menor que n?

n = int(input('Digite um numero: \t'))
m = int(input('Digite um numero: \t'))
o = n-m
p = o//m
q = p*m
print('O maior multiplo de m: \t', q)

# q = (n-1)//m
# mt = q*m
# print(mt)