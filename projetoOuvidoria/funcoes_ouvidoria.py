from configuracoes_iniciais import *

def exibir_menu():
    """
        Exibe o menu de opções do sistema para o usuário.
    :return: Uma string do menu formatada
    """

    return ("=" * 40 + "\n" +
            "1) Listagem das Manifestações\n"
            "2) Listagem das Manifestacoes filtradas por tipo\n"
            "3) Criar uma nova Manifestação\n"
            "4) Exibir quantidade de manifestações\n"
            "5) Pesquisar uma manifestação pelo código\n"
            "6) Excluir uma manifestacao pelo codigo\n"
            "7) Sair do Sistema\n" +
            "=" * 40)

def listar_manifestacoes(conexao):
    """
    Lista todas as manifestações cadastradas.
    Se não houver manifestações, informa ao usuário.
    :param conexao: Conexao do banco de dados
    :return: Lista com as manifestacoes
    """
    sql_listagem = "select codigo, avaliacao, tipo, descricao_manifestacao from manifestacoes"
    lista_de_manifestacoes = listarBancoDados(conexao, sql_listagem)

    manifestacoes = []

    if not lista_de_manifestacoes:
        manifestacoes.append("Nao ha manifestacoes")
        return manifestacoes

    else:
        for codigo, avaliacao, tipo, descricao_manifestacao in lista_de_manifestacoes:
            manifestacoes.append(f"{codigo}. Nota {avaliacao}. Tipo da manifestacao: {tipo}\n"
                                 f" {descricao_manifestacao}\n" +
                                 "-" * 30)

        return manifestacoes

def listar_manifestacao_por_tipo(conexao, tipo):
    """
    Lista as manifestacoes de acordo com o tipo
    :param conexao: Conexao do banco de dados
    :param tipo: Tipo da manifestacao para listar
    :return: lista de manifestacoes filtradas pelo tipo
    """

    sql_listagem_por_tipo = "select codigo, avaliacao, descricao_manifestacao from manifestacoes where tipo = %s"
    lista_de_manifestacoes_filtradas = listarBancoDados(conexao, sql_listagem_por_tipo, (tipo, ))

    manifestacoes = []

    if not lista_de_manifestacoes_filtradas:
        manifestacoes.append(f"Nao ha manifestacoes do tipo {tipo}")
        return manifestacoes

    else:
        for codigo, avaliacao, descricao_manifestacao in lista_de_manifestacoes_filtradas:
            manifestacoes.append(f"{codigo}. Nota {avaliacao}.\n"
                                 f" {descricao_manifestacao}\n" +
                                 "-" * 30)

        return manifestacoes

def criar_manifestacao(conexao, nota, tipo, manifestacao):
    """
    Permite ao usuário criar uma nova manifestação e adicioná-la à lista.
    Exibe o código da manifestação cadastrada.
    """
    dados = [nota, tipo, manifestacao]

    inserir_manifestacao = "insert into manifestacoes (avaliacao, tipo, descricao_manifestacao) values (%s, %s, %s)"
    codigo_atual = insertNoBancoDados(conexao, inserir_manifestacao, dados)


    return (f"Manifestacao cadastrada com sucesso. Seu codigo e {codigo_atual} "
            f"{f'Obrigado pela nota {nota}' if nota >= 3 else 
            '\nLamentamos que sua experiência não tenha sido satisfatória. '
            'Seu feedback é muito importante para melhorarmos nossos serviços.'}")

def exibir_quantidade_manifestacoes(conexao):
    """
    Exibe a quantidade total de manifestações cadastradas.
    """
    quantidade_de_manifestacoes = listarBancoDados(conexao, "select count(*) from manifestacoes")
    return f"Quantidade de manifestacoes cadastradas: {quantidade_de_manifestacoes[0][0]}"

def pesquisar_manifestacao(conexao, codigo):
    """
    Permite ao usuário pesquisar uma manifestação pelo código.
    Se o código for inválido, informa o erro.
    :param conexao: Conexao do banco de dados
    :param codigo: Codigo para pesquisar a manifestacao
    :return: string formatada com a manifestacao pesquisada
    """
    manifestacao_pesquisada = []

    if  codigo not in codigos_filmes_disponiveis or codigo < 0:
        manifestacao_pesquisada.append("\033[31;1mCodigo pesquisado invalido\033[m")
        return manifestacao_pesquisada

    else:

        sql_manifestacao = "select * from manifestacoes where codigo = %s"
        codigo_pesquisado = listarBancoDados(conexao,sql_manifestacao, (codigo, ))


        for codigo, avaliacao, tipo, descricao_manifestacao, data in codigo_pesquisado:
            manifestacao_pesquisada.append(f"{codigo}. Nota {avaliacao}. Tipo da manifestacao: {tipo}\n"
                                           f" {descricao_manifestacao}\n" +
                                           f"Criada em {data}\n" + "-" * 30)

        return manifestacao_pesquisada

def excluir_manifestacao(conexao, codigo):

    if quantidade_de_manifestacoes == 0:
        return "Nao ha manifestacoes"

    else:
        manifestacao_para_excluir = listarBancoDados(conexao, "Select * from manifestacoes where codigo = %s",
                                                     (codigo, ))
        manifestacao_para_excluir = manifestacao_para_excluir[0]

        sql_excluir = "delete from manifestacoes where codigo = %s"
        manifestacao_excluida = excluirBancoDados(conexao, sql_excluir, (codigo, ))

        return (f"Manifestacao: Codigo {manifestacao_para_excluir[0]}. Nota {manifestacao_para_excluir[1]}. Tipo da "
                f"manifestacao: {manifestacao_para_excluir[2]}\n {manifestacao_para_excluir[3]}\n Excluida com sucesso")



# Funcoes para o programa principal da ouvidoria:

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
    print("-" * 30)
    tipo = input("Digite o tipo da manifestacao: ").strip().capitalize()

    while tipo not in tipos_de_manifestacoes:
        print(f"\033[31;1mTIPO DE MANIFESTACAO INVALIDA.\033[m")
        print("Tipos de manifestacoes: ")
        for tipo in tipos_de_manifestacoes:
            print(tipo)
        tipo = input("Digite o tipo da manifestacao: ").strip().capitalize()

    return tipo

def validar_codigo_da_manifestacao():
    while True:
        try:
            codigo = int(input("Digite o codigo da manisfetacao: "))

            if codigo > 0 and codigo in codigos_filmes_disponiveis:
                return codigo

            else:
                print("\033[31;1mCódigo inválido!\033[m")

        except ValueError:
            print("\033[31;1mEntrada invalida!\033[m")