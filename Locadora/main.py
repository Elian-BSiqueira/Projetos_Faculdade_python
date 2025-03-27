from time import sleep
from funcoes.funcoes_locadora import *


opcaoEscolhida = None
while opcaoEscolhida != 4:
    print(exibirmenu())


    try:
        opcaoEscolhida = int(input('Digite sua opcao: '))
        sleep(0.5)
    except ValueError:
        sleep(0.5)
        print('\033[31;1mERRO. DIGITE APENAS NUMEROS\033[m')
        sleep(0.5)
        continue

    if opcaoEscolhida == 1:
        lista = listarfilmes(conexao)
        for mensag in lista:
            print(mensag)
            sleep(1)

    elif opcaoEscolhida == 2:
        lista = listarfilmes(conexao)
        for mensag in lista:
            print(mensag)
            sleep(1)

        while True:

            try:
                numeroDoFilmeEscolhido = int(input('Digite o numero do filme que deseja alugar: '))
                if 0 < numeroDoFilmeEscolhido in codigos_filmes_disponiveis:
                    break

                else:
                    print('\033[31mNumero invalido. Escolha um filme da lista\033[m')

            except ValueError:
                print('\033[31;1mERRO. DIGITE APENAS NUMEROS\033[m')

        print(alugarfilme(conexao, numeroDoFilmeEscolhido))

    elif opcaoEscolhida == 3:

        nomeFilme = input("Digite o nome do filme que deseja adionar a lista de filmes disponiveis para alugar: ")
        sinopseFilme = input("Digite a sinopse do filme: ")

        while True:
            try:
                anoFilme = int(input("Digite o ano do filme: "))

                if anoFilme > 0:
                    break

                else:
                    print('\033[31;1mAno Invalido\033[m')

            except ValueError:
                print('\033[31;1mERRO. DIGITE APENAS NUMEROS\033[m')

        dados = [nomeFilme, sinopseFilme, anoFilme]

        print(adicionarFilme(conexao, dados))

    elif opcaoEscolhida == 4:
        print('Programa encerrado com sucesso')
        encerrarConexao(conexao)
        break

    else:
        print('\033[31;1mOpcao invalida! Escolha entre 1 e 4. \033[m')
        sleep(1)
