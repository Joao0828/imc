def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif imc < 25:
        return "peso adequado"
    elif imc < 30:
        return "sobrepeso"
    elif imc < 35:
        return "obesidade grau I"
    elif imc < 40:
        return "obesidade grau II"
    else:
        return "obesidade grau III"

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, digite números válidos para peso e altura.")
    
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
