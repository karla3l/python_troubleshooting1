# Um natural é dito triangular se ele é produto de três naturais consecutivos. 
# Exemplo: 120 é triangular, pois 4⋅5⋅6=120. Dado um natural, ele é triangular?

num = int(input("Digite um numero natural: \t"))
n=1
triangular = n * (n+1) * (n+2)
while triangular < num:
    n+=1
    triangular = n * (n+1) * (n+2)

if triangular == num:
    print(f'{num} É triangular')
    print(f'({n}) * ({n+1}) * ({n+2}) = {num}')
else:
    print(f'{num} Não é triangular')
#_________________________________________________________________
    
# Um natural é dito triangular se ele é produto de três naturais consecutivos. 
# Exemplo: 120 é triangular, pois 4⋅5⋅6=120. Dado um triangular, quais são os três naturais?

triangular = int(input("Digite um número triangular: "))

# Vamos iterar por possíveis valores de n até encontrar os três naturais
n = 1
while True:
    produto = n * (n + 1) * (n + 2) // 6

    if produto == triangular:
        # Encontramos os três naturais consecutivos
        naturais_consecutivos = (n, n + 1, n + 2)
        break
    
    if produto > triangular:
        # Não encontramos, interrompemos o loop
        naturais_consecutivos = None
        break

    n += 1

if naturais_consecutivos:
    print(f"Os três naturais consecutivos para o número triangular {triangular} são: {naturais_consecutivos}")
else:
    print("Não foi possível encontrar três naturais consecutivos para o número triangular dado.")

