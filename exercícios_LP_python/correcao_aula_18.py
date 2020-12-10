'''
Exercício extra
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

As perguntas são:

a) Telefonou para a vítima?
b) Esteve no local do crime?
c) Mora perto da vítima?
d) Devia para a vítima?
e) Já trabalhou com a vítima?

O programa em Python deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a:
2 questões ela deve ser classificada como SUSPEITA.
3 ou 4 questões como CÚMPLICE.
5 questões como ASSASSINO.
Caso contrário, ele será classificado como INOCENTE.

Importante: Usar pelo menos uma função.
'''

def verificar_participacao():
    respostas = []
    classificacao = 5
    print("Responda as seguintes perguntas para sabermos sua participação no crime. Digite apenas S ou N.")
    respostas.append(input("Você telefonou para a vítima? ").upper())
    respostas.append(input("Esteve no local do crime? ").upper())
    respostas.append(input("Mora perto da vítima? ").upper())
    respostas.append(input("Devia para a vítima? ").upper())
    respostas.append(input("Já trabalhou com a vítima? ").upper())
    for c in range(5):
        if respostas[c] == "N":
            classificacao -= 1
    if classificacao < 2:
        print("Classificação da participação no crime: INOCENTE.")
    elif classificacao == 2:
        print("Classificação da participação no crime: SUSPEITA.")
    elif classificacao == 3 or classificacao == 4:
        print("Classificação da participação no crime: CÚMPLICE.")
    else:
        print("Classificação da participação no crime: ASSASINO.")


verificar_participacao()
print("=-=- FIM DO PROGRAMA -=-=")

