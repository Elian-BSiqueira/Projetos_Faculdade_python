from funcoes_ouvidoria import *

def main():
    """
    Função principal que gerencia o fluxo do programa.
    Mantém o loop do menu até que o usuário escolha sair.
    """
    opcao = -1

    while opcao != 7:
        print(exibir_menu())
        while True:
            try:
                opcao = int(input("Digite sua opcao: "))

                if 1 <= opcao <= 7:
                    break

                else:
                    print(f"\033[31;1mDigite uma opcao entre 1 e 7\033[m")

            except ValueError:
                print("\033[31;1mERRO. Digite uma opcao entre 1 e 7\033[m")


        quantidade_de_manifestacoes = atualizar_quantidade(conexao)

        codigos_disponiveis = atualizar_codigos(conexao)

        if opcao == 1:
            sleep(0.5)
            if quantidade_de_manifestacoes == 0:
                print("\033[31mNao ha manifestacoes cadastradas\033[m")
            else:
                lista_manifestacoes = listar_manifestacoes(conexao)
                listagem_das_manifestacoes(lista_manifestacoes)

        elif opcao == 2:
            if quantidade_de_manifestacoes == 0:
                print("Nao ha manifestacoes cadastradas")
                continue

            tipo = validar_tipo_manifestacao()
            if cancelar_operacao(tipo):
                continue

            lista_filtrada_manifestacoes = listar_manifestacao_por_tipo(conexao, tipo)
            listagem_das_manifestacoes(lista_filtrada_manifestacoes)

        elif opcao == 3:
            nota = validar_inteiro("Digite uma nota entre 1 e 5: ", 1, 5)
            if cancelar_operacao(nota):
                continue

            tipo = validar_tipo_manifestacao()


            manifestacao = input("Descreva sua manifestacao (Deixe em branco para cancelar): ")

            if not manifestacao.strip():
                print("\033[33mOperação cancelada.\033[m")
                continue

            print(criar_manifestacao(conexao, nota, tipo, manifestacao))

        elif opcao == 4:
            print(exibir_quantidade_manifestacoes(conexao))

        elif opcao == 5:
            sleep(0.5)
            if quantidade_de_manifestacoes == 0:
                print("Nao ha manifestacoes cadastradas")
                continue

            codigo = validar_codigo_da_manifestacao()
            if cancelar_operacao(codigo):
                continue

            manifestacao_pesquisada = pesquisar_manifestacao(conexao, codigo)
            for item in manifestacao_pesquisada:
                print(item)
            sleep(1)

        elif opcao == 6:
            if quantidade_de_manifestacoes == 0:
                print("Nao ha manifestacoes cadastradas")
                continue

            codigo = validar_codigo_da_manifestacao()

            if cancelar_operacao(codigo):
                continue

            print(excluir_manifestacao(conexao, codigo))
        elif opcao == 7:
            print("\033[32;1mSaindo do programa. Obrigado por usar\033[m")
            encerrarConexao(conexao)


if __name__ == "__main__":
    main()