# Dada uma letra, qual a sua posição no alfabeto, sendo ‘a’ a posição 1 e ‘z’ a posição 26?

letra = input('Digite uma letra: \t')

if len(letra) == 1:
    if 'a' <= letra <= 'z':
        posicao = ord(letra) - ord('a') + 1
        print(f"A posição da letra '{letra}' no alfabeto é {posicao}")
    elif 'A' <= letra <= 'Z':
        posicao = ord(letra) - ord('A') + 1
        print(f"A posição da letra '{letra}' no alfabeto é {posicao}")
    else:
        print('Por favor, digite uma letra do alfabeto.')
else:
    print('Por favor, digite uma única letra.')
