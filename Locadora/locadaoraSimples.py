from time import sleep

filmes = ['Os Banshees de Inisherin', 'Barbie', 'John Wick 4: Baba Yaga', 'Creed III', 'Top Gun: Maverick',
          'Assassinos da Lua das Flores', 'Close', 'Sorria', 'Homem-Aranha: Através do Aranhaverso', 'Oppenheimer']

opcaoEscolhida = None
while opcaoEscolhida != 5:
    print('=' * 30)
    print('Locadora'.center(28))
    print('=' * 30)
    print('Opcao 1 - Listar filmes')
    print('Opcao 2 - Alugar filme')
    print('Opcao 3 - Devolver filme')
    print('Opcao 4 - Adicionar filme')
    print('Opcao 5 - Sair')

    opcaoEscolhida = input('Digite sua opcao: ')
    sleep(0.5)

    if opcaoEscolhida.isdigit():
        opcaoEscolhida = int(opcaoEscolhida)
    else:
        print('\033[31;1mERRO. DIGITE APENAS NUMEROS\033[m')
        sleep(0.5)
        continue

    if opcaoEscolhida == 1:
        if filmes:
            print('Filmes disponíveis:')
            for i, filme in enumerate(filmes, start=1):
                print(f'{i} - {filme}')
                sleep(0.3)
        else:
            print('Nenhum filme disponível no momento.')

    elif opcaoEscolhida == 2:
        if not filmes:
            print('Nenhum filme disponível para alugar.')
        else:
            print('Filmes disponíveis:')
            for i, filme in enumerate(filmes, start=1):
                print(f'{i} - {filme}')
                sleep(0.3)
            numeroDoFilmeEscolhido = input('Digite o número do filme que deseja alugar: ')
            if numeroDoFilmeEscolhido.isdigit():
                numeroDoFilmeEscolhido = int(numeroDoFilmeEscolhido)
                if 0 < numeroDoFilmeEscolhido <= len(filmes):
                    filmeAlugado = filmes.pop(numeroDoFilmeEscolhido - 1)
                    print(f'Filme {filmeAlugado} alugado com sucesso')
                else:
                    print('\033[31mNúmero inválido. Escolha um filme da lista.\033[m')
            else:
                print('\033[31mERRO. DIGITE APENAS NUMEROS\033[m')
        sleep(0.3)

    elif opcaoEscolhida == 3:
        filmeDevolvido = input('Digite o nome do filme devolvido: ').strip().title()
        filmes.append(filmeDevolvido)
        print(f'Filme {filmeDevolvido} devolvido com sucesso')

    elif opcaoEscolhida == 4:
        adicionarFilme = input('Digite o nome do filme que deseja adicionar: ').strip().title()
        while len(adicionarFilme) == 0:
            print("Filme não pode ser vazio")
            adicionarFilme = input('Digite o nome do filme que deseja adicionar: ').strip().title()
        filmes.append(adicionarFilme)
        print(f'Filme {adicionarFilme} adicionado com sucesso')

    elif opcaoEscolhida == 5:
        print('Programa encerrado com sucesso')

    else:
        print('\033[31mOpcao invalida! Escolha entre 1 e 5.\033[m')
        sleep(1)
