# Sejam dois naturais n≥p, podemos calcular seu número binomial como... Dados dois naturais n≥p, qual seu número binomial?

# Função para calcular o fatorial de um número
def fatorial(num):
    if num == 0:
        return 1
    else:
        fat = 1
        for i in range(1, num + 1):
            fat *= i
        return fat

# Leitura dos valores de n e p
n = int(input("Digite o valor de n: "))
p = int(input("Digite o valor de p: "))

# Verificação de n >= p
if n >= p:
    resultado = fatorial(n) / (fatorial(p) * fatorial(n - p))
    print(f"C({n}, {p}) = {resultado}")
else:
    print("n deve ser maior ou igual a p.")
