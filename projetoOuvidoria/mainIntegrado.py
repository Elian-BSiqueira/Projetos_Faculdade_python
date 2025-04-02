from time import sleep
from funcoes_ouvidoria import * # Codigo de autoria de Daniel Abella, professor da unifacisa


def listagem_das_manifestacoes(lista):
    for manifestacao in lista:
        print(manifestacao)
        sleep(0.5)


def validar_opcao(texto):
    while True:
        try:
            opcao = int(input(texto))

            if 1 <= opcao <= 7:
                return opcao


            else:
                print("\033[31;1mDigite um valor entre 1 e 7\033[m")

        except ValueError:
            print("\033[31;1mERRO. Digite um valor valido\033[m")

def validar_tipo_manifestacao():
    tipos_de_manifestacoes = ["Sugestao", "Elogio", "Reclamacao"]
    print("Tipos de manifestacoes: ")
    for tipo in tipos_de_manifestacoes:
        print(tipo)
    tipo = input("Digite o tipo da manifestacao: ").capitalize().strip()

    while tipo not in tipos_de_manifestacoes:
        print(f"\033[31;1mTIPO DE MANIFESTACAO INVALIDA.\033[m")
        print("Tipos de manifestacoes: ")
        for tipo in tipos_de_manifestacoes:
            print(tipo)
        tipo = input("Digite o tipo da manifestacao: ").capitalize().strip()

    return tipo

def validar_codigo_da_manifestacao():
    while True:
        try:
            codigo = int(input("Digite o codigo da manisfetacao: "))

            if 0 < codigo <= quantidade_de_manifestacoes:
                return codigo

            else:
                print("\033[31;1mCódigo inválido!\033[m")

        except ValueError:
            print("\033[31;1mEntrada invalida!\033[m")

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

            print("Tipos de manifestacoes: Sugestao\nElogio\nReclamacao")
            tipos_de_manifestacoes = ["Sugestao", "Elogio", "Reclamacao"]
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

        elif opcao == 6:
            codigo = validar_codigo_da_manifestacao()
            print(excluir_manifestacao(conexao, codigo))


        elif opcao == 7:
            print("Saindo do programa. Obrigado por usar")
            encerrarConexao(conexao)


if __name__ == "__main__":
    main()