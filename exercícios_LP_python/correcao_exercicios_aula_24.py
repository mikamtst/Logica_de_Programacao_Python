#Exercício 1

#Crie um programa em Python que preencha uma matriz (lista de lista) 
#7x2 com números inteiros informados pelo usuário. 
#Mostre a quantidade de elementos entre 10 e 20 (inclusive).


matriz = []

for i in range(7):
    linha = []
    for j in range(2):
       linha.append(int(input("Entre com um número: ")))
    matriz.append(linha)

print("\n")
contar = 0
for lista in matriz:
    for elemento in lista:
        if elemento >=10 and elemento <=20:
            contar+=1

print("Quantidade de elementos entre 10 e 20: ", contar)

#Exercício 2

#Faça um programa em Python que realiza a soma de duas matrizes 2x2.
#Importante: O usuário entrará com os valores (números inteiros) que preencherá
#as duas matrizes (a e b). Mostrar na tela a terceira matriz (c) com a soma de a + b.

def preencher_matriz(matriz):
    for i in range(2):
        linha = []
        for j in range(2):
            linha.append(int(input("Entre com um número: ")))
        matriz.append(linha)
    return matriz

def mostrar_matriz(matrizA,matrizB,matrizC):
     for i in range(len(matrizA)):
        if(i==1):
            print("\n          +            =")
        else:
            print("\n")
        for j in range(len(matrizA)):
          print(matrizA[i][j], end='    ')
        print(end='    ')
        for j in range(len(matrizB)):
          print(matrizB[i][j], end='    ')
        print(end='    ')
        for j in range(len(matrizC)):
          print(matrizC[i][j], end='    ')


matrizA = []
matrizB = []
matrizC = []

print("-- Preencher a matriz A --")
matrizA = preencher_matriz(matrizA)


print("-- Preencher a matriz B --")
matrizB = preencher_matriz(matrizB)

for listaA,listaB in zip(matrizA,matrizB):
    linha = []
    for elementoA, elementoB in zip(listaA,listaB):
        linha.append(elementoA+elementoB)
    matrizC.append(linha)

mostrar_matriz(matrizA,matrizB,matrizC)


#Exercicio 3
#Faça um programa em Python que preencha uma matriz 5x5 de números reais. 
#Calcule e mostre a soma dos elementos da diagonal secundária.

matriz = [[float(input(f"Matriz {i}x{j}:  ")) for j in range(5)] for i in range(5)]

soma = 0
pos = -1
for linha in matriz:
    print("Linha: ",linha)
    print("--> Somando... :", linha[pos])
    soma += linha[pos]
    pos -= 1

print("Soma da diagonal secundária: ",soma)


#Exercicio 4
#Faça um programa em Python que preencha uma matriz 8x8 de números inteiros. 
#Calcule e mostre a media dos elementos da diagonal principal.

def preencher_matriz(matriz,tam1,tam2):
    for i in range(tam1):
        linha = []
        for j in range(tam2):
            linha.append(int(input("Entre com um número: ")))
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()

def soma_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(i==j):
                soma+=matriz[i][j]
    return soma/len(matriz)

matriz = []

tam1 = 8
tam2 = 8

if(tam1==tam2):
    print("-- Preencher matriz --")
    matriz = preencher_matriz(matriz, tam1, tam2)

    print("-- Matriz --")
    mostrar_matriz(matriz)
    
    print("Média da diagonal principal: ", soma_diagonal(matriz))
else:
    print("Diagonal principal é possível apenas em matriz quadrada")

#Exercicio 4 - Modelo 2
#Faça um programa em Python que preencha uma matriz 8x8 de números inteiros. 
#Calcule e mostre a media dos elementos da diagonal principal.

tam = 8
matriz = [[int(input(f"Matriz {i}x{j}:  ")) for j in range(tam)] for i in range(tam)]

soma = 0
pos = 0
for linha in matriz:
    soma += linha[pos]
    pos += 1

print("Média da diagonal principal: ",soma/tam)

#********************************************************************************************************************************************

#Exercicio 5 - Modelo 1
#Crie um programa em Python que receba do usuário 20 números inteiros. 
#Armazenar os números ordenadamente na matriz 5x4. Mostrar na tela a matriz resultante.

def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()

numeros = [int(input(f"Digite o {n+1}º número: ")) for n in range(0, 20)]
numeros.sort()
matriz = []
inicio = 0
fim = 4

for i in range(0, 5):
    print("Alimentando matriz: ",numeros[inicio:fim] )
    matriz.append(numeros[inicio:fim])
    inicio = fim
    fim += 4

mostrar_matriz(matriz)


#Exercicio 5 - Modelo 2
#Crie um programa em Python que receba do usuário 20 números inteiros. 
#Armazenar os números ordenadamente na matriz 5x4. Mostrar na tela a matriz resultante.
num=1
lista = []
matrix =[]
for i in  range(20):
    lista.append(int(input(f"Digite o {num}º numero da matriz : ")))
    num += 1
listaORD = sorted(lista)
while listaORD !=[]:
    matrix.append(listaORD[:4])
    listaORD = listaORD[4:]
for listaORD in matrix:
    for elemento in listaORD:
        print(elemento, end=' ')
    print()

#Exercicio 5
'''
Elabore um programa que preencha uma matriz 4x4 com números inteiros informados pelo usuário
e verifique se a matriz forma o chamado quadrado mágico e mostre na tela uma mensagem.
Um quadrado mágico é formado quando a soma dos elementos de cada linha é igual a soma dos elementos
de cada coluna, igual à soma dos elementos da diagonal principal e, também igual à soma dos elementos
da diagonal secundária.
'''
#Exemplo de quadrado mágico para teste:
#https://www.google.com.br/search?q=exemplo+de+quadrado+m%C3%A1gico+4x4&tbm=isch&ved=2ahUKEwiulr2B6ovsAhUQNLkGHaGjAYAQ2-cCegQIABAA&oq=exemplo+de+quadrado+m%C3%A1gico+4x4&gs_lcp=CgNpbWcQA1DOigRYlo8EYJSRBGgAcAB4AIABeIgBnwOSAQMyLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=8NNxX67eGZDo5OUPoceGgAg&bih=571&biw=1188

def preencher_matriz(matriz,tam1,tam2):
    for i in range(tam1):
        linha = []
        for j in range(tam2):
            linha.append(int(input("Entre com um número: ")))
        matriz.append(linha)
    return matriz


def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end='   ')
        print()


def verificar(ver,primeiro):
    #for i in ver:
    #    if(i!=primeiro):
    #        return False
    #return True

    if all(num == primeiro for num in ver):
        return True
    return False



def ver_quadrado_magico(matriz):
    soma_secundaria = 0
    soma_principal = 0
    soma_linha = []
    soma_coluna = []

    for i in range(len(matriz)):
        total_linha=0
        for j in range(len(matriz)):
            if(i+j==len(matriz)-1):
                soma_secundaria+=matriz[i][j]
            if(i==j):
                soma_principal+=matriz[i][j]
            total_linha+=matriz[i][j]
        soma_linha.append(total_linha)

    for j in range(len(matriz)):
        total_colunas=0
        for i in range(len(matriz)):
            total_colunas+=matriz[i][j]
        soma_coluna.append(total_colunas)

    linha = verificar(soma_linha,soma_linha[0])
    coluna = verificar(soma_coluna,soma_coluna[0])

    print("Soma das linhas: ", soma_linha)
    print("Soma das colunas: ", soma_coluna)
    print("Soma da diagonal principal: ", soma_principal)
    print("Soma da diagonal secundária: ",soma_secundaria)
    if(coluna and linha and soma_principal==soma_secundaria):
        print("É um quadrado mágico")
    else:
        print("Não é um quadrado mágico")

matriz = []

print("Qual o tamanho da matriz? ")
tam1 = 4
tam2 = 4

print("-- Preencher matriz --")
matriz = preencher_matriz(matriz,tam1,tam2)

print("-- Matriz --")
mostrar_matriz(matriz)

ver_quadrado_magico(matriz)

