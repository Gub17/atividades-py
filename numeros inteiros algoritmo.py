# Inicializa uma lista para armazenar os números
numeros = []

# Solicita ao usuário que insira 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Calcula o maior, menor e a soma dos números
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Exibe os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma de todos os números é: {soma}")
