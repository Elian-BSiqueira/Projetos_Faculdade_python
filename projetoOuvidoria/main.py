# Etapa 1
from time import sleep

opcao = -1
listaDeManifestacoes = []
while opcao != 5:
    print("=" * 30)
    print("1) Listagem das Manifestações\n"
          "2) Criar uma nova Manifestação\n"
          "3) Exibir quantidade de manifestações\n"
          "4) Pesquisar uma manifestação por código\n"
          "5) Sair do Sistema")
    print("=" * 30)

    while True:
        try:
            opcao = int(input("Digite sua opcao: "))

            if 0 < opcao <= 5:
                break

            else:
                print("Digite uma opcao entre 1 e 5")

        except ValueError:
            print("\033[31mERRO. Digite uma opcao valida\033[m")

    if opcao == 1:
        if not listaDeManifestacoes:
            print("Nao ha manifestacoes")
            sleep(1)

        else:
            for contador, manif in enumerate(listaDeManifestacoes, start=1):
                sleep(0.3)
                print(f"{contador}) {manif}")
                sleep(0.5)

    elif opcao == 2:
        manifestacao = input("Descreva sua manifestacao: ")
        listaDeManifestacoes.append(manifestacao)
        sleep(0.3)
        print(f"Manifestacao cadastrada com sucesso. Seu codigo e {len(listaDeManifestacoes)}")
        sleep(1)

    elif opcao == 3:
        print(f"Existem {len(listaDeManifestacoes)} manifestacoes cadastradas")
        sleep(1)

    elif opcao == 4:

        while True:
            try:
                codigo = int(input("Digite o codigo da manisfetacao: "))
                break

            except ValueError:
                print("Entrada invalida!")

        print(f"{codigo}) {listaDeManifestacoes[codigo - 1]}")
        sleep(1)

    elif opcao == 5:
        print("Saindo do programa. Obrigado por usar")







