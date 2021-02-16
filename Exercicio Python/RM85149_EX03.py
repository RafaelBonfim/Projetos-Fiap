print("Escolha número de 1 a 5 para votar:")
print('1-Segunda-Feira 2-Terça-feira 3-Quarta-feira 4-Quinta-feira 5- Sexta-feira 6-Resultado')
#os votos estão zerados
segundafeira=0
tercafeira=0
quartafeira=0
quintafeira=0
sextafeita=0
n1 = 0
#Digite 6 para mostrar o resultado da votação

while n1 != 6 : #enquanto variavel for diferente de 5 faça
    n1=int(input("Digite seu voto:"))
    if n1==1:
        print("Votou Segunda-Feira")
        segundafeira=segundafeira+1 #acumulador
    elif n1==2:
        print("Votou Terça-Feira")
        tercafeira=tercafeira+1
    elif n1==3:
        print("Votou Quarta-Feita")
        quartafeira=quartafeira+1
    elif n1==4:
        print("Votou Quinta-Feira")
        quintafeira=quintafeira+1
    elif n1==5:
        print("Votou Sexta-Feira")
        sextafeita=segundafeira+1

print("==FIM DA VOTAÇÃO==")
print("Segunda-Feira obteve",segundafeira,"votos.")
print("Terça-Feita obteve",tercafeira, "votos.")
print("Quarta-Feita obteve",quartafeira, "votos.")
print("Quinta-Feira obteve",quintafeira, "votos.")
print("Sexta-Feita obteve",sextafeita, "votos.")