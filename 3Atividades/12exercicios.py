# Dado o preço da etiqueta de um produto e o código da condição de pagamento,
# qual o valor a ser pago pelo produto? Utilize a seguinte tabela de referência:
#_______________________________________________________________________________
#
#Código	       Condição de pagamento
# 1	           À vista em dinheiro ou cheque, recebe 10% de desconto
# 2	           No cartão de débito ou PIX, recebe 5% de desconto
# 3	           Em duas vezes, preço normal de etiqueta sem juros
# 4	           Em três vezes, preço normal de etiqueta mais juros de 10%
#_______________________________________________________________________________

preco_etiqueta = float(input("Digite o preço da etiqueta do produto: R$ "))
codigo_condicao = int(input("Digite o código da condição de pagamento: "))

if codigo_condicao == 1:
    valor_pago = preco_etiqueta - (preco_etiqueta * 0.10)  # Desconto de 10%
elif codigo_condicao == 2:
    valor_pago = preco_etiqueta - (preco_etiqueta * 0.05)  # Desconto de 5%
elif codigo_condicao == 3:
    valor_pago = preco_etiqueta  # Preço normal em duas vezes
elif codigo_condicao == 4:
    valor_pago = preco_etiqueta + (preco_etiqueta * 0.10)  # Juros de 10%
else:
    print("Código de condição de pagamento inválido.")
    exit()

print(f"O valor a ser pago pelo produto é: R$ {valor_pago:.2f}")
