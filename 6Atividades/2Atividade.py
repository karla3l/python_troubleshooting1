# Qual o intervalo de inteiros de cada item a seguir? (escrever cada intervalo em uma linha)
""" [0, 10[    # de 0-9 sem contar o 10
    ]10, 0]    # de 9-0 sem contar o 10
    [-10, 10]  # todos os numeros do -10-10
    [100, 1]   # todos os numeros do 100-1 """ 
    
    
# Intervalo de 0 a 9 (incluindo 0, excluindo 10)
intervalo_0_a_9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Intervalo de 10 a 0 (incluindo ambos)
intervalo_10_a_0 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Intervalo de -10 a 10 (incluindo ambos)
intervalo_menos10_a_10 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Intervalo de 100 a 1 (incluindo ambos)
intervalo_100_a_1 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 
                    79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 
                    56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 
                    33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 
                    10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Imprimir os intervalos
print("[0, 10[:", intervalo_0_a_9)
print("[10, 0]:", intervalo_10_a_0)
print("[-10, 10]:", intervalo_menos10_a_10)
print("[100, 1]:", intervalo_100_a_1)
