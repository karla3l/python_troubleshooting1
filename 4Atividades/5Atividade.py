# Dada uma letra, ela é vogal ou consoante?

letra = input('Digite uma letra: \t')

if len(letra) == 1:
    letra = letra.lower()  # Converte a letra para minúscula para facilitar a verificação

    if 'a' <= letra <= 'z':
        if letra in 'aeiou':
            print(f"'{letra}' é uma vogal.")
        else:
            print(f"'{letra}' é uma consoante.")
    else:
        print('Por favor, digite uma letra do alfabeto.')
else:
    print('Por favor, digite uma única letra.')
