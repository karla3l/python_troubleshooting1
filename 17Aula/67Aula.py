print("Início")
for externo in range(1, 4):
    print(">", end=" ")
    for interno in range(1, 6):
        print(externo, interno, sep="", end=" ")
    print()  # Adiciona uma quebra de linha após a conclusão de cada linha interna
print("Fim")

#___________________________________________________________________________________

i = 12
for j in range(1, i + 1):
    print("", j, end="")
    if j % 5 == 0 or j % 3 == 0:
        print(" A", end="")
    if i % j == 0:
        print(" B", end="")
    else:
        print(" C", end="")