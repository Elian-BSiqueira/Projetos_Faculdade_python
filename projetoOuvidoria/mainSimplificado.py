# Etapa 1
# Codigo simplificado sem usar bloco try except ou verificacoes complexas

opcao = -1
listaDeManifestacoes = []
while opcao != 5:
    print("1) Listagem das Manifestações\n"
          "2) Criar uma nova Manifestação\n"
          "3) Exibir quantidade de manifestações\n"
          "4) Pesquisar uma manifestação por código\n"
          "5) Sair do Sistema")

    opcao = int(input("Digite sua opcao: "))

    while opcao <= 0 or opcao > 5:
        # verifica se a entrada é uma opção valida

        print(f"\033[31mERRO. opcao invalida\033[m")
        opcao = int(input("Digite sua opcao: "))

    if opcao == 1:
        if not listaDeManifestacoes:
            print("Nao ha manifestacoes")

        else:
            contador = 1
            for manif in listaDeManifestacoes:
                print(f"{contador}) {manif}")

    elif opcao == 2:
        manifestacao = input("Descreva sua manifestacao: ")
        listaDeManifestacoes.append(manifestacao)
        print(f"Manifestacao cadastrada com sucesso. Seu codigo e {len(listaDeManifestacoes)}")

    elif opcao == 3:
        print(f"Existem {len(listaDeManifestacoes)} manifestacoes cadastradas")

    elif opcao == 4:
        codigo = int(input("Digite o codigo da manisfetacao: "))
        print(f"{codigo}) {listaDeManifestacoes[codigo - 1]}")

    elif opcao == 5:
        print("Saindo do programa. Obrigado por usar")