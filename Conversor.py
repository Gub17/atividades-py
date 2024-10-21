def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def menu():
    print("Conversor de Temperaturas com Múltiplas Escalas")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Celsius")
    print("6. Converter de Kelvin para Fahrenheit")
    print("7. Sair do programa")

while True:
  menu()
  opcao = int(input("Escolha uma opção: "))

  if opcao == 7:
      print("Saindo do programa...")
      break
  
  temperatura = float(input("Digite o valor da temperatura: "))

  if opcao == 1:
      print(f"{temperatura}°C é igual a {celsius_para_fahrenheit(temperatura)}°F")
  elif opcao == 2:
      print (f"{temperatura}°C é igual a {celsius_para_kelvin(temperatura)}K")
  elif opcao == 3:
      print(f"{temperatura}°F é igual a {fahrenheit_para_celsius(temperatura)}°C")
  elif opcao == 4:
      print(f"{temperatura}°F é igual a {fahrenheit_para_celsius(temperatura)}K")
  elif opcao == 5:
      print(f"{temperatura}K é igual a {kelvin_para_celsius(temperatura)}°C")
  elif opcao == 6:
      print(f"{temperatura}K é igual a {kelvin_para_fahrenheit(temperatura)}°F")
  else:
      print("Opção inválida, por pavor tente novamente.")