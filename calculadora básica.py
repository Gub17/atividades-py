def calculadora_basica():
    while True:
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        operacao = input("Digite o número da operação desejada: ")

        if operacao == '5':
            print("Saindo da calculadora...")
            break

        if operacao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if operacao == '1':
                    resultado = num1 + num2
                    print(f"O resultado da soma é: {resultado}")
                elif operacao == '2':
                    resultado = num1 - num2
                    print(f"O resultado da subtração é: {resultado}")
                elif operacao == '3':
                    resultado = num1 * num2
                    print(f"O resultado da multiplicação é: {resultado}")
                elif operacao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"O resultado da divisão é: {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")

            except ValueError:
                print("Erro: Por favor, digite um número válido.")
        else:
            print("Operação inválida. Tente novamente.")

# Chamada da função
calculadora_basica()
