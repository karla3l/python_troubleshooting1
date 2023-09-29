# Você pode omitir o valor inicial se quiser começar do zero:
print("Contando do 0 até o 9...")
for cont in range(10):
    print(cont)
#____________________________________________________________

# Você pode especificar o tamanho do teu "passo" na contagem:
print("Contagem de 5 em 5...")
inicio = 0
fim = 50
passo = 5
for cont in range(inicio, fim, passo):
    print(cont)
#____________________________________________________________

# Se o teu passo for negativo e o valor inicial for maior que o valor final, a contagem será regressiva:
print("Contagem regressiva...")
for cont in range(10, 0, -1):
    print(cont)
#____________________________________________________________

# Assim como qualquer estrutura que possui corpo, se este for composto por apenas uma linha de código, pode ir na mesma linha que a estrutura:
print("Contagem regressiva...")
for cont in range(10, 0, -1): print(cont)
#____________________________________________________________

# Assim como qualquer estrutura que possui corpo, não se esqueça do dois-pontos separando a declaração da estrutura do seu corpo!
#Observação: Assim como no while, o for pode nunca ser executado!
print("Valendo!")
for cont in range(0, 10, -1):
    print(cont)
print("Fim!")


