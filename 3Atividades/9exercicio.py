# Em certa região, o preço pelo fornecimento de energia elétrica depende do consumo em kWh, 
# conforme a seguinte tabela:
#________________________________
#
#   Faixa (kWh)	     Preço (R$)
#   Até 500	         0,40
#   Acima de 500	 0,65
#________________________________
# Dado o consumo de uma residência em kWh, qual o preço da energia a ser pago?

consumo = float(input("Digite o consumo de uma residência em kwh: \t"))
p1 = 0.40
p2 = 0.65
if consumo > 500:
    print("O valor a ser pago eh: \t", p2)
else:
    print("O valor a ser pago eh: \t", p1)



