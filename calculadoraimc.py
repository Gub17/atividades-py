def calcular_imc(peso, altura) :
    imc = peso/(altura ** 2)
    return imc

def classificar_imc(imc) :
    if imc < 18.5 :
        return "abaixo do peso"
    elif 18.5 <= imc <24.9:
        return "peso normal"
    elif 25 <= imc < 29.9:
        return "sobrepeso"
    elif 30 <= imc < 34.9:
        return "obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "obesidade grau 2"
    else:
        return "obesidade grau 3"
    
    def main():
        peso = float(input("digite o peso em kg: "))
        altura = float(input("digite a altura em metros: "))

        imc = calcular_imc(peso, altura)
        classificacao =
        classificar_imc(imc)

        print(f "seu IMC é: {imc: .2f}")
        print(f "classificassao:
              {classificassao}") 

              if__name__== "__main__":
              main()
              


    