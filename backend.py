# Integrantes do grupo: NICOLE DE LUCENA MACEDO, MARIANA ARAUJO AZEVEDO, RAYANNE VARELO ALVES CALDAS, CLARA LOURDES CUNHA MARQUES

def listar_reclamacoes(lista):
    if len(lista) > 0:
        print("\nLista de reclamações:")
        for item in range(len(lista)):
            print(str(item + 1) + ") " + lista[item])
    else:
        print("Não existem reclamações a serem exibidas")

def adicionar_reclamacao(lista):
    nova_reclamacao = input("Digite a sua reclamação: ")
    lista.append(nova_reclamacao)
    print("Reclamação adicionada com sucesso!")

def pesquisar_reclamacao(lista):
    posicao = int(input("Insira o código da reclamação: "))
    if posicao >= 1 and posicao <= len(lista):
        print("A reclamação selecionada é:", lista[posicao - 1])
    else:
        print("O código informado é inválido")

def atualizar_reclamacao(lista):
    posicao = int(input("Insira o código da reclamação que deseja atualizar: "))
    if posicao >= 1 and posicao <= len(lista):
        novo_texto = input("Digite o novo texto da reclamação: ")
        lista[posicao - 1] = novo_texto
        print("Reclamação atualizada com sucesso!")
    else:
        print("O código informado é inválido")

def remover_reclamacao(lista):
    posicao = int(input("Insira o código da reclamação que deseja remover: "))
    if posicao >= 1 and posicao <= len(lista):
        lista.pop(posicao - 1)
        print("Remoção realizada com sucesso!")
    else:
        print("O código informado é inválido")

def obter_quantidade_reclamacoes(lista):
    print("Quantidade total de reclamações:", len(lista))