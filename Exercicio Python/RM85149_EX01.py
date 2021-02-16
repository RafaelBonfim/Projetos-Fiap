#Script para cálculo de IMC (Índice de Massa Corporal).
#Solicitando dados do usuário.
peso = float(input(' Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m) '))
#Cálculando IMC.
#Verificando categoria do IMC.
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 16:
    print('Baixo peso Grau III')
elif imc < 17:
    print("Baixo peso Grau II")
elif imc < 18.5:
    print("Baixo peso Grau I")
elif imc < 25:
    print("Peso Ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")


    # IMC e Categoria
    #              >= 40,00 Obesidade Grau III
    # >= 35,00 and <= 39,99 Obesidade Grau II
    # >= 30,00 and <= 34,99 Obesidade Grau I
    # >= 25,00 and <= 29,99 Sobrepeso
    # >= 18,50 and <= 24,99 Peso ideal
    # >= 17,00 and <= 18,49 Baixo peso Grau I
    # >= 16,00 and <= 16,99 Baixo peso Grau II
    # <  16,00              Baixo peso Grau III
