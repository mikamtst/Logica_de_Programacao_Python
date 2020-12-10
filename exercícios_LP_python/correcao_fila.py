
def menu():
    return input("""
    1 - Imprimir nova senha
    2 - Imprimir nova senha (prioridade)
    3 - Relatório: Mostrar fila de atendimento
    4 - Atender paciente
    5 - Sair
    Sua opção: """)

from collections import deque

fila = deque([])
listaPref = []
senha = 0
senhaPref = 0
opcoes = ("1","2","3","4","5")
opcao = menu()
while opcao not in opcoes:
    print("Opção inválida!")
    print("=-"*12)
    opcao = input("Digite uma opção válida: ")

while opcao in opcoes:
    while opcao not in opcoes:
        print("Opção inválida!")
        opcao = input("Digite uma opção válida: ")

    if opcao == "1":
        senha+=1
        fila.append(f"{'S'+str(senha)}")

    elif opcao == "2":
        senhaPref += 1
        fila.append(f"{'P'+str(senhaPref)}")



    elif opcao == "3":
        fila = list(fila)
        fila.sort()
        print()
        print("=-"*15)
        print(f"{'ORDEM DA FILA':^30}")
        print("=-" * 15)
        pos = 0
        for i in fila:
            pos += 1
            print(f"\tA {pos}º posição é: {i}", end='\n')
        print("=-"*15)

    elif opcao == "4":
        fila = list(fila)
        fila.sort()
        if(len(fila)!=0):
            del fila[0]
        else:
            print("Fila vazia")


    elif opcao == "5":
        print()
        print("=-"*15)
        print(f"{'FIM DO PROGRAMA':^30}")
        print("=-"*15)
        exit()

    opcao = menu()
