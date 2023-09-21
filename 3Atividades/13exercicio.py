# Para descobrir o peso ideal de uma pessoa, calcula-se o Índice de Massa Corporal (IMC) 
# utilizando a seguinte fórmula: imc=peso/altura2. Dados o peso e a altura de uma pessoa, 
# de acordo com a tabela a seguir, qual é o seu IMC e a sua condição atual?
""" Condição	    IMC em mulheres	     IMC em homens
    Abaixo do peso	IMC<19.1	         IMC<20.7
    No peso ideal	19.1≤IMC<25.8	     20.7≤IMC<26.4
    Acima do peso	25.8≤IMC	         26.4≤IMC """

    

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# Escolha do gênero
print("Escolha o gênero:")
print("1. Mulher")
print("2. Homem")
genero_escolhido = int(input("Digite o número correspondente ao seu gênero: "))

# Calcular IMC e determinar a condição
imc = peso / (altura * altura)

if genero_escolhido == 1:
    if imc < 19.1:
        print('Condição: Abaixo do peso')
    elif imc < 25.8:
        print('Condição: No peso ideal')
    else:
        print('Condição: Acima do peso')
elif genero_escolhido == 2:
    if imc < 20.7:
        print('Condição: Abaixo do peso')
    elif imc < 26.4:
        print('Condição: No peso ideal')
    else:
        print('Condição: Acima do peso')
else:
    print('Escolha de gênero inválida.')

print('Seu IMC é:', imc)
