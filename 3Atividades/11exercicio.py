# Dado o código de determinado produto, qual a sua classificação? 
# Utilize a seguinte tabela de referência:
#_________________________________________________
#
#Código	                        Classificação
# 1	                            Alimento não perecível
# 2, 3 ou 4	                    Alimento perecível
# 5 ou 6	                    Vestuário
# 7	                            Higiene pessoal
# 8 até 15	                    Limpeza e utensílios domésticos
# Qualquer outro código	        Inválido
#_________________________________________________

codigo = int(input("Digite um código: \t"))
if codigo == 1:
    print("Alimento não perecível")
elif codigo == 2:
    print("Alimento perecivel")
elif codigo == 3:
    print("Alimento perecivel")
elif codigo == 4:
    print("Alimento perecivel")
elif codigo == 5:
    print("Vestuario")
elif codigo == 6:
    print("Vestuario")
elif codigo == 7:
    print("Higiene pessoal")
elif codigo == 8:
    print("Limpeza e utensílios domésticos")
elif codigo == 9:
    print("Limpeza e utensílios domésticos")
elif codigo == 10:
    print("Limpeza e utensílios domésticos")
elif codigo == 11:
    print("Limpeza e utensílios domésticos")
elif codigo == 12:
    print("Limpeza e utensílios domésticos")
elif codigo == 13:
    print("Limpeza e utensílios domésticos")
elif codigo == 14:
    print("Limpeza e utensílios domésticos")
elif codigo == 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Invalido")
