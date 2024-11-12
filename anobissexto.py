# Função para verificar se um ano é bissexto
def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicitar o ano ao usuário
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Verificar se o ano é bissexto
if verificar_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")