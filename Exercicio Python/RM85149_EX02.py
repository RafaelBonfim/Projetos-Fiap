tipo_assinatura = input("Informar tipo de assinatura")
valor_anual = float(input("Inserir o faturamento anual da assinatura"))
if tipo_assinatura=="basic":
    bonus = valor_anual * 0.3
    print("O valor a ser pago é {}".format(bonus))
elif tipo_assinatura=="Silver":
     bonus = valor_anual * 0.2
     print('O valor a ser pago é {}'.format(bonus))
elif tipo_assinatura=="Gold":
     bonus = valor_anual * 0.1
     print('O valor a ser pago é {}'.format(bonus))
elif tipo_assinatura=="Platinum":
     bonus = valor_anual * 0.05
     print('O valor a ser pago é {}'.format(bonus))
