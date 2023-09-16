# Dados dois inteiro, qual o inteiro no meio deles? Se houver empate, escolha o menor inteiro.
# Exemplo: entre 1 e 3, o meio é o 2; entre 1 e 6 é 3; entre 0 e 6 é 3; entre 12 e 18 é 15.
# (obs: esse calculo é usado em muitos algoritmos importantes como o mergesort)

num1 = int(input('Digite um numero: \t'))
num2 = int(input('Digite um numero: \t'))

meio = (num1+num2)/2
print('O meio dos numeros é: \t', meio)