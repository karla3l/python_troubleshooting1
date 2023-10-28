# Programa de caixa de loja. Ler uma sequência de triplas que correspondem às informações dos produtos comprados:
# quantidade, preço unitário, nome do produto. A sequência termina quando for lida uma tripla de zeros. 
# Escrever, em uma linha para cada produto, seu nome e o preço total. Escrever na última linha o preço total da compra.

total_compra = 0  # Variável para rastrear o preço total da compra

while True:
    quantidade = int(input("Digite a quantidade (ou 0 para encerrar): "))
    if quantidade == 0:
        break  # Se a quantidade for zero, encerra o loop
    
    preco = float(input("Digite o preço unitário: "))
    nome = input("Digite o nome do produto: ")

    # Calcula o preço total para este produto
    preco_total = quantidade * preco     

    # Adiciona o preço total ao preço total da compra
    total_compra += preco_total

    # Imprime o nome e o preço total deste produto
    print(f"Produto: {nome}, Preço Total: {preco_total:.2f}")

# Imprime o preço total da compra
print(f"Preço Total da Compra: {total_compra:.2f}")
