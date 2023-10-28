# Dada uma sequência de duplas de números, representando valores e seus respectivos pesos, 
# seguida por uma dupla de zeros, qual a média ponderada desconsiderando a dupla de zeros?

soma_produto = 0  # Inicializa a soma dos produtos
soma_pesos = 0  # Inicializa a soma dos pesos

while True:
    valor, peso = map(int, input("Digite um valor e um peso (ou 0 0 para encerrar): ").split())
    if valor == 0 and peso == 0:
        break  # Encerra o loop quando encontrar a dupla de zeros

    soma_produto += valor * peso
    soma_pesos += peso

if soma_pesos == 0:
    print("Nenhum valor foi fornecido.")
else:
    media_ponderada = soma_produto / soma_pesos
    print(f"Média Ponderada: {media_ponderada:.2f}")
