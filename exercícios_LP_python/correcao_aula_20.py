'''
Faça uma função que receba uma data (DD/MM/AAAA) e retorne uma string no
formato: dia de mesdoano de ano

Validação: Fazer uma função para validar ano bissexto caso o mês digitado for fevereiro

Exemplo_1:
Digite uma data no formato DD/MM/AAAA: 29/06/2009
29 de junho de 2009

Exemplo_2:
Digite uma data no formato DD/MM/AAAA: 29/02/1981
— Em 1981 fevereiro foi de 28 dias
'''

def bissexto(ano):
    if(ano%4==0):
        if(ano%100==0):
            if(ano%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def dma(dia, mes, ano):
    if dia <= 31:
        meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                 'Novembro', 'Dezembro')
        mesPorextenso = meses[mes - 1]
        if mesPorextenso == 'Fevereiro' and dia >= 30:
            print("Fevereiro só tem 29 ou 28 dias!")
        elif mesPorextenso == 'Fevereiro' and dia > 28 and bissexto(ano)==False:
            print("Fevereiro só tem 28 dias em anos não bissextos!")
        elif((mesPorextenso == 'Abril' or mesPorextenso == 'Junho' or mesPorextenso == 'Setembro'
        or mesPorextenso == 'Novembro') and dia==31):
            print("O Mes de ",mesPorextenso," não tem 31 dias")
        else:
            print("%d de %s de %i" % (dia, mesPorextenso, ano))
    else:
        print("Dia inválido")

data = input("Digite uma data no formato DD/MM/AAAA: ")
dia,mes,ano = data.split('/')
dma(int(dia),int(mes),int(ano))