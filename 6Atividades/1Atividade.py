""" Uma faculdade oferece um curso que prepara os candidatos a obter licença estadual para 
corretores de imóveis. No ano passado, dez estudantes que concluíram esse curso prestaram 
o exame. A universidade quer saber como foi o desempenho dos seus estudantes nesse exame. 
Você foi contratado para escrever um programa que resuma os resultados.
Ler o nome e o resultado de cada estudante, sendo o resultado um valor booleano (True ou False)
que indica se o estudante foi aprovado ou reprovado no exame. Escrever a quantidade de 
estudantes aprovados, a quantidade de reprovados, e se mais de oito estudantes foram aprovados, 
escrever “Bônus ao instrutor!”. """

# Inicialize as variáveis para contar os aprovados e reprovados
aprovados = 0
reprovados = 0

# Inicialize a variável para contar o número de estudantes
contador = 0

# Use um loop while para ler os resultados de cada estudante
while contador < 10:
    nome = input("Digite o nome do estudante: ")
    resultado_str = input("Digite o resultado do estudante (True para aprovado, False para reprovado): ")
    resultado = resultado_str.lower() == 'true'  # Correção: comparação com 'true' em minúsculas
    
    # Verifique o resultado e atualize as contagens
    if resultado:
        aprovados += 1
    else:
        reprovados += 1
    
    contador += 1

# Escreve a quantidade de estudantes aprovados e reprovados
print("Quantidade de estudantes aprovados:", aprovados)
print("Quantidade de estudantes reprovados:", reprovados)

# Verifique se mais de oito estudantes foram aprovados
if aprovados > 8:
    print("Bônus ao instrutor!")
