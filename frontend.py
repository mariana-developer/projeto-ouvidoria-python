# Integrantes do grupo: NICOLE DE LUCENA MACEDO, MARIANA ARAUJO AZEVEDO, RAYANNE VARELO ALVES CALDAS, CLARA LOURDES CUNHA MARQUES

from backend import *

reclamacoes = []
opcao = 0

while opcao != 7:
    print("\n------------ Menu ------------ \n1) Listar reclamações registradas, \n2) Adicionar uma nova reclamação, \n3) Pesquisar uma reclamação pelo código, \n4) Atualizar uma reclamação existente, \n5) Remover uma reclamação pelo código, \n6) Mostrar a quantidade de reclamações cadastradas, \n7) Sair.")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        listar_reclamacoes(reclamacoes)

    elif opcao == 2:
        adicionar_reclamacao(reclamacoes)

    elif opcao == 3:
        pesquisar_reclamacao(reclamacoes)

    elif opcao == 4:
        atualizar_reclamacao(reclamacoes)

    elif opcao == 5:
        remover_reclamacao(reclamacoes)

    elif opcao == 6:
        obter_quantidade_reclamacoes(reclamacoes)

    elif opcao != 7:
        print("Opção inválida")

print("Obrigado por usar nosso sistema!")