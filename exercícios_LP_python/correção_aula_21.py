# Exercício 1
def ex1a():
    dados = {'Ana': 'Colegio Bandeirantes',
             'João': 'Colegio Santo Antonio',
             'Matheus': 'FIAP School',
             'Maria': 'Colegio FAAP'}
    print(dados)

# Exercício 2:
def ex2():
    filmes = {'Filme_1': {'Ano': 2020, 'Ator': 'Jack Nicholson'},
              'Filme_2': {'Ano': 2019, 'Ator': 'Robert de Niro'},
              'Filme_3': {'Ano': 2018, 'Ator': 'Al Pacino'},
              'Filme_4': {'Ano': 2017, 'Ator': 'Denzel Washington'},
              'Filme_5': {'Ano': 2015, 'Ator': 'Tom Hanks'}}

    for tipo, tipo2 in filmes.items():
        print('\nFilme: ', tipo)
        print('Ano: ', tipo2['Ano'])
        print('Ator Principal: ', tipo2['Ator'])


# Exercicio 3
def ex3a():
    def pesquisa(RA):
        busca = input("Digite um RA para saber se está ativo: ")
        if busca in RA.values():
            print("RA de", list(RA.keys())[list(RA.values()).index(busca)], "está ativo")
        else:
            print("RA inativo ou inexistente")

    RA = {'Aline': '12345', 'Beatriz': '12346', 'Caique': '12347'}
    pesquisa(RA)

# Exercicio 4
def ex4a():
    continuar = True
    esfera = 0
    limpeza = 0
    cabo_conector = 0
    quebrado_inutiliz = 0

    print("Para encerrar digite 0 na identificação!")
    while continuar == True:
        identificacao = int(input("Digite o número de identificação do mouse: "));
        if (identificacao == 0):  # FINALIZA
            continuar = False
        else:
            print("", "-" * 30, "\n           Mouse", "\n", "-" * 30,
                  "\n1 -> necessita da esfera"
                  "\n2 -> necessita de limpeza"
                  "\n3 -> necessita troca do cabo ou conector"
                  "\n4 -> quebrado ou inutilizado")
            entrada = int(input("Situação: "))
            while entrada < 0 or entrada > 4 or entrada == None:
                entrada = int(input("Resposta Inválida. Digite novamente! Situação: "))
            if entrada == 1:
                esfera += 1
            elif entrada == 2:
                limpeza += 1
            elif entrada == 3:
                cabo_conector += 1
            elif entrada == 4:
                quebrado_inutiliz += 1

    total = esfera + limpeza + cabo_conector + quebrado_inutiliz
    if (total != 0):
        print("\nQuantidade de mouses: ", total, "\n\nSituação\t\t\t\t\t\t\t\t\t\t\tQuantidade\t\t\t\tPercentual")
        print("\n1 - Necessita da esfera\t\t\t\t\t\t\t\t", esfera, "\t\t\t\t\t\t", esfera * 100 / total, "%")
        print("2 - Necessita da limpeza\t\t\t\t\t\t\t", limpeza, "\t\t\t\t\t\t", limpeza * 100 / total, "%")
        print("3 - Necessita de troca do cabo ou conector\t\t\t", cabo_conector, "\t\t\t\t\t\t",
              cabo_conector * 100 / total, "%")
        print("4 - Quebrado ou inutilizado\t\t\t\t\t\t\t", quebrado_inutiliz, "\t\t\t\t\t\t",
              quebrado_inutiliz * 100 / total, "%")

    print("\nPrograma encerrado!")
