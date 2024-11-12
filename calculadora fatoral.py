def calcular_fatorial(n):
    # Verifica se o número é negativo, zero ou positivo
    if n < 0:
        return "O fatorial não está definido para números negativos."
    elif n == 0:
        return 1
    
    fatorial = 1
    contador = n
    
    # Loop while para calcular o fatorial
    while contador > 1:
        fatorial *= contador
        contador -= 1
    
    return fatorial

def main():
    # Solicita um número ao usuário
    try:
        numero = int(input("Digite um número inteiro não negativo: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return
    
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")

if __name__ == "__main__":
    main()
