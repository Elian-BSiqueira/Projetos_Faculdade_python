from time import sleep

filmes = ['Os Banshees de Inisherin', 'Barbie', 'John Wick 4: Baba Yaga', 'Creed III', 'Top Gun: Maverick',
    'Assassinos da Lua das Flores', 'Close', 'Sorria', 'Homem-Aranha: Através do Aranhaverso', 'Oppenheimer']

def exibirmenu():
    # Exibe o menu do programa

    print('=' * 30)
    print('Locadora'.center(28))
    print('=' * 30)
    print('Opcao 1 - Listar filmes\n'
          'Opcao 2 - Alugar filme\n'
          'Opcao 3 - Devolver filme\n'
          'Opcao 4 - Adicionar filme\n'
          'Opcao 5 - Sair')

def listarfilmes():
    # Lista os filmes disponiveis para algugar

    if filmes:
        print('Filmes disponíveis:')
        for i, filme in enumerate(filmes, start=1):
            print(f'{i} - {filme}')
            sleep(0.3)
    else:
        print('Nenhum filme disponível no momento.')

def alugarfilme():
    # Permine o usuario alugar um filmes

    sleep(0.5)
    if not filmes:
        print('Nenhum filme disponivel')
        return

    listarfilmes()

    while True:
        try:
            numeroDoFilmeEscolhido = int(input('Digite o numero do filme que deseja alugar: '))
            if 0 < numeroDoFilmeEscolhido < len(filmes) + 1:
                filmeAlugado = filmes.pop(numeroDoFilmeEscolhido - 1)
                print(f'filme {filmeAlugado} alugado com sucesso')
                break

            else:
                print('\033[31mNumero invalido. Escolha um filme da lita\033[m')

        except ValueError:
            print('ERRO. DIGITE APENAS NUMEROS')
        sleep(0.3)

def devolverFilme():
    # Permite o usuario devolver um filme

    filmeDevolvido = input('Digite o nome do filme devolvido: ').strip().title()
    filmes.append(filmeDevolvido)
    print(f'Filme {filmeDevolvido} Devolvido com sucesso')

def adicionarFilme():
    # Permite o usuario adicionar um filme para alugar

    AdicionarFilme = input("Digite o nome do filme que deseja adionar a lista de filmes disponiveis para alugar: ")
    filmes.append(AdicionarFilme)
    print(f"Filme {AdicionarFilme} adicionado com sucesso")


# Loop Principal do programa
opcaoEscolhida = None
while opcaoEscolhida != 5:
    exibirmenu()


    try:
        opcaoEscolhida = int(input('Digite sua opcao: '))
        sleep(0.5)
    except ValueError:
        sleep(0.5)
        print('\033[31mERRO. DIGITE APENAS NUMEROS\033[m')
        sleep(0.5)
        continue

    if opcaoEscolhida == 1:
        listarfilmes()

    elif opcaoEscolhida == 2:
        alugarfilme()

    elif opcaoEscolhida == 3:
        devolverFilme()

    elif opcaoEscolhida == 4:
        adicionarFilme()

    elif opcaoEscolhida == 5:
        print('Programa encerrado com sucesso')

    else:
        print('\033[31mOpcao invalida! Escolha entre 1 e 6. \033[m')
        sleep(1)
