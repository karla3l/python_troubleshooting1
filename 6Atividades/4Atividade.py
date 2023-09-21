# Dada a quantidade de estudantes da turma de Algoritmos, seguida pelas notas das provas de 
# cada estudante, qual a maior nota e a média das notas dessa turma?

quantidade_estudantes = int(input("Digite a quantidade de estudantes na turma: "))

# Inicialize a variável para armazenar a soma das notas
soma_notas = 0

# Inicialize a variável para armazenar a maior nota
maior_nota = float('-inf')

# Inicialize a variável para contar os estudantes
contador_estudantes = 0

# Loop para ler as notas de cada estudante e calcular a soma das notas e a maior nota
while contador_estudantes < quantidade_estudantes:
    nota = float(input(f"Digite a nota do estudante {contador_estudantes + 1}: "))
    soma_notas += nota
    
    # Verifica se é a maior nota até agora
    if nota > maior_nota:
        maior_nota = nota

    contador_estudantes += 1

# Calcula a média das notas
media_notas = soma_notas / quantidade_estudantes

# Imprime a maior nota e a média das notas
print(f"A maior nota na turma é: {maior_nota}")
print(f"A média das notas na turma é: {media_notas}")
