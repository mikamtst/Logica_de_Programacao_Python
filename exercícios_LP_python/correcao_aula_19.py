#Exercicio 3
print("** Maior número da tupla **")
def maiorTupla (tupla):#tupla = (1,2,3,4,5,6,7,80,9,10,11,12,13,14,15)
     maior = max(tupla) #a função max retorna o maior valor da tupla
     return maior

tupla = (1,2,3,4,5,6,7,80,9,10,11,12,13,14,15)
print(maiorTupla(tupla))

#Exercicio 4
#list() - converte uma tupla em lista
def mediaTupla (tupla):
     lista = list(tupla);
     media = sum(lista) / len(lista)
     return media
tupla = (1.8,2,3,4.2)
print(mediaTupla(tupla))

#Exercicio 5
def maiorStringTupla(tupla) :
     maiorString = 0
     posicaoDaMaior = 0
     lista = list(tupla)
     for i in lista:
         if (len(i) > maiorString):
             maiorString = len(i)
             posicaoDaMaior = i
     return posicaoDaMaior
tupla = ("FIAP", "Paulista", "TDS", "Primeiro Ano")
print(maiorStringTupla(tupla))


print(maior_palavra())


#Exercicio 6
def combinacoes(nomes):
    for a in range(len(nomes)):
        for b in range(len(nomes)):
            if (nomes[a] != nomes[b]) and (b > a):
                print(nomes[a], "e", nomes[b])

nomes = ("Micaela", "Bia", "Nali", "Diana", "Eva", "Fabia")
combinacoes(nomes)