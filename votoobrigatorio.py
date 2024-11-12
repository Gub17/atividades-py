def classificar_idade(idade):
    if idade < 16:
        return "Não permitido"
    elif 16 <= idade <= 17 or idade >= 65:
        return "Opcional"
    elif 18 <= idade <= 65:
        return "Obrigatório"
    else:
        return "Categoria não definida"

# Exemplos de uso
idades = [15, 16, 20, 65, 70, 80]
resultados = {idade: classificar_idade(idade) for idade in idades}

for idade, resultado in resultados.items():
    print(f"Idade {idade}: {resultado}")