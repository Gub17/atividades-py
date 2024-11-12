# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Inicializa as variáveis
soma = 0
contador = 1

# Loop while para calcular a soma
while contador <= numero:
    soma += contador
    contador += 1

# Exibe o resultado
print(f"A soma de todos os números de 1 até {numero} é {soma}.")
