from time import sleep
from funcoes_ouvidoria import *

def validar_opcao(texto):
    while True:
        try:
            opcao = int(input(texto))

            if 1 <= opcao <= 5:
                return opcao


            else:
                print("\033[31;1mDigite um valor entre 1 e 5\033[m")

        except ValueError:
            print("\033[31;1mERRO. Digite um valor valido\033[m")





lista_manifestacoes = listar_manifestacoes(conexao)

def main():
    """
    Função principal que gerencia o fluxo do programa.
    Mantém o loop do menu até que o usuário escolha sair.
    """
    opcao = -1

    while opcao != 5:
        print(exibir_menu())
        opcao = validar_opcao("Digite sua opcao: ")

        if opcao == 1:
            sleep(0.5)
            for manifestacao in lista_manifestacoes:
                print(manifestacao)
                sleep(0.5)

        elif opcao == 2:
            nota = validar_opcao("Digite uma nota entre 1 e 5: ")
            manifestacao = input("Descreva sua manifestacao: ")
            print(criar_manifestacao(conexao, nota, manifestacao))

        elif opcao == 3:
            print(exibir_quantidade_manifestacoes(conexao))

        elif opcao == 4:
            sleep(0.5)
            for manifestacao in lista_manifestacoes:
                print(manifestacao)
                sleep(0.5)

            while True:
                try:
                    codigo = int(input("Digite o codigo da manisfetacao: "))

                    if 0 < codigo <= quantidade_de_manifestacoes:
                        print(pesquisar_manifestacao(conexao, codigo))
                        break

                    else:
                        print("\033[31;1mCódigo inválido!\033[m")

                except ValueError:
                    print("\033[31;1mEntrada invalida!\033[m")

        elif opcao == 5:
            print("Saindo do programa. Obrigado por usar")
            encerrarConexao(conexao)


if __name__ == "__main__":
    main()