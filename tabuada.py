# Solicita ao usuário para inserir um número
numero = int(input("Digite um número para ver a tabuada: "))

# Inicializa a variável contador
contador = 1

# Inicia o loop while
while contador <= 10:
    # Calcula o resultado da multiplicação
    resultado = numero * contador
    
    # Imprime o resultado
    print(f"{numero} x {contador} = {resultado}")
    
    # Incrementa o contador
    contador += 1