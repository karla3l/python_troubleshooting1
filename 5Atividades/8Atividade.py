# Gerar uma senha aleatória de 8 dígitos com letras maiúsculas, minúsculas e inteiros.

import random

# Caracteres possíveis para a senha (letras maiúsculas, minúsculas e números)
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Gera uma senha aleatória de 8 dígitos
senha_aleatoria = (
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres) +
    random.choice(caracteres)
)

# Exibe a senha gerada
print(f"Senha aleatória: {senha_aleatoria}")
