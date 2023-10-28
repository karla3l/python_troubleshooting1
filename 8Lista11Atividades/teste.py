sequencia = input("Digite uma sequência de números: ")
reverso = ""

for i in range(len(sequencia) - 1, -1, -1):
    reverso += sequencia[i]

print("Sequência invertida:", reverso)
