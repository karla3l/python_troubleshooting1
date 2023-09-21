# Determinar as raízes ou zero de uma função do 2º grau consiste em determinar os pontos de 
# intersecção da parábola com o eixo das abscissas no plano cartesiano. 
# Dada a função f(x)=ax2+bx+c, podemos determinar sua raiz considerando f(x)=0, 
# dessa forma obtemos a equação do 2º grau ax2+bx+c=0, que pode ser resolvida pelo método
# resolutivo de Bháskara. Neste, as raízes são x1​=−b+Δ/2a e x2​=−b−Δ/2a, onde Δ=b2−4ac. 
# Dados os valores das constantes a, b e c, quais as raízes da equação? Caso a=0, 
# escrever "Não é equação de segundo grau". Caso Δ<0, escrever "Não existe raiz". 
# Caso Δ=0, escrever a raiz e a mensagem "Raiz única". Caso Δ>0, escrever as duas raízes.


# Coeficientes da equação do segundo grau: ax^2 + bx + c
a = float(input("Digite o coeficiente a: \t"))
b = float(input("Digite o coeficiente b: \t"))
c = float(input("Digite o coeficiente c: \t"))

if a == 0:
    print("Não é uma equação de segundo grau")
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"Raiz única: {raiz}")
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        print(f"Raízes: x1 = {x1}, x2 = {x2}")
