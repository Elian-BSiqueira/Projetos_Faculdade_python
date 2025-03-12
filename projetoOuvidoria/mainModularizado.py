from time import sleep


def exibir_menu():
    """
    Exibe o menu de opções do sistema para o usuário.
    """
    print("=" * 30)
    print("1) Listagem das Manifestações\n"
          "2) Criar uma nova Manifestação\n"
          "3) Exibir quantidade de manifestações\n"
          "4) Pesquisar uma manifestação por código\n"
          "5) Sair do Sistema")
    print("=" * 30)


def validar_opcao():
    """
    Solicita ao usuário uma opção válida entre 1 e 5.
    Retorna a opção escolhida.
    """
    while True:
        try:
            opcao = int(input("Digite sua opcao: "))
            if 0 < opcao <= 5:
                return opcao
            else:
                print("Digite uma opcao entre 1 e 5")
        except ValueError:
            print("\033[31mERRO. Digite uma opcao valida\033[m")


def listar_manifestacoes(lista):
    """
    Lista todas as manifestações cadastradas.
    Se não houver manifestações, informa ao usuário.
    """
    if not lista:
        print("Nao ha manifestacoes")
        sleep(1)
    else:
        for contador, manif in enumerate(lista, start=1):
            sleep(0.3)
            print(f"{contador}) {manif}")
            sleep(0.5)


def criar_manifestacao(lista):
    """
    Permite ao usuário criar uma nova manifestação e adicioná-la à lista.
    Exibe o código da manifestação cadastrada.
    """
    manifestacao = input("Descreva sua manifestacao: ")
    lista.append(manifestacao)
    sleep(0.3)
    print(f"Manifestacao cadastrada com sucesso. Seu codigo e {len(lista)}")
    sleep(1)


def exibir_quantidade_manifestacoes(lista):
    """
    Exibe a quantidade total de manifestações cadastradas.
    """
    print(f"Existem {len(lista)} manifestacoes cadastradas")
    sleep(1)


def pesquisar_manifestacao(lista):
    """
    Permite ao usuário pesquisar uma manifestação pelo código.
    Se o código for inválido, informa o erro.
    """
    while True:
        try:
            codigo = int(input("Digite o codigo da manisfetacao: "))
            if 0 < codigo <= len(lista):
                print(f"{codigo}) {lista[codigo - 1]}")
                sleep(1)
                return
            else:
                print("Código inválido!")
        except ValueError:
            print("Entrada invalida!")


def main():
    """
    Função principal que gerencia o fluxo do programa.
    Mantém o loop do menu até que o usuário escolha sair.
    """
    opcao = -1
    listaDeManifestacoes = []

    while opcao != 5:
        exibir_menu()
        opcao = validar_opcao()

        if opcao == 1:
            listar_manifestacoes(listaDeManifestacoes)
        elif opcao == 2:
            criar_manifestacao(listaDeManifestacoes)
        elif opcao == 3:
            exibir_quantidade_manifestacoes(listaDeManifestacoes)
        elif opcao == 4:
            pesquisar_manifestacao(listaDeManifestacoes)
        elif opcao == 5:
            print("Saindo do programa. Obrigado por usar")


if __name__ == "__main__":
    main()
