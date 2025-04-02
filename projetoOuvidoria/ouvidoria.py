from time import sleep
from funcoes_ouvidoria import *

def main():
    """
    Função principal que gerencia o fluxo do programa.
    Mantém o loop do menu até que o usuário escolha sair.
    """
    opcao = -1

    while opcao != 7:
        print(exibir_menu())
        opcao = validar_opcao("Digite sua opcao: ")
        quantidade_de_manifestacoes = listarBancoDados(conexao, "select count(*) from manifestacoes")
        quantidade_de_manifestacoes = quantidade_de_manifestacoes[0][0]
        lista_manifestacoes = listar_manifestacoes(conexao)

        if opcao == 1:
            sleep(0.5)
            listagem_das_manifestacoes(lista_manifestacoes)

        elif opcao == 2:
            tipo = validar_tipo_manifestacao()
            lista_filtrada_manifestacoes = listar_manifestacao_por_tipo(conexao, tipo)
            listagem_das_manifestacoes(lista_filtrada_manifestacoes)

        elif opcao == 3:
            nota = validar_opcao("Digite uma nota entre 1 e 5: ")
            tipo = validar_tipo_manifestacao()

            manifestacao = input("Descreva sua manifestacao: ")
            print(criar_manifestacao(conexao, nota, tipo, manifestacao))

        elif opcao == 4:
            print(exibir_quantidade_manifestacoes(conexao))

        elif opcao == 5:
            sleep(0.5)
            listagem_das_manifestacoes(lista_manifestacoes)
            codigo = validar_codigo_da_manifestacao()
            manifestacao_pesquisada = pesquisar_manifestacao(conexao, codigo)
            for item in manifestacao_pesquisada:
                print(item)
            sleep(1)

        elif opcao == 6:
            codigo = validar_codigo_da_manifestacao()
            print(excluir_manifestacao(conexao, codigo))


        elif opcao == 7:
            print("Saindo do programa. Obrigado por usar")
            encerrarConexao(conexao)


if __name__ == "__main__":
    main()