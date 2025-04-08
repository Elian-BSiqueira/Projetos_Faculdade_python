from mysql.connector.constants import flag_is_set
from funcoes_mysql import *
from config import *
from time import sleep

conexao = criarConexao(host, user, password, database)

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
        return ["Nao ha manifestacoes"]

    else:
        for i, (codigo, avaliacao, tipo, descricao_manifestacao) in enumerate(lista_de_manifestacoes,start=1):
            manifestacoes.append(f"{i}. Nota {avaliacao}.\nCodigo. {codigo} Tipo da manifestacao: {tipo}\n"
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
    if tipo is None:
        return ["Operacao cancelada"]

    sql_listagem_por_tipo = "select codigo, avaliacao, descricao_manifestacao from manifestacoes where tipo = %s"
    lista_de_manifestacoes_filtradas = listarBancoDados(conexao, sql_listagem_por_tipo, (tipo, ))

    if not lista_de_manifestacoes_filtradas:
        return [f"Nao ha manifestacoes do tipo {tipo}"]

    manifestacoes = []


    for i, (codigo, avaliacao, descricao_manifestacao) in enumerate(lista_de_manifestacoes_filtradas, start=1):
        manifestacoes.append(f"{i}.\nCodigo. {codigo}\n Nota {avaliacao}.\n"
                            f" {descricao_manifestacao}\n" +
                            "-" * 30)

    return manifestacoes

def criar_manifestacao(conexao, nota, tipo, manifestacao):
    """
    Permite ao usuário criar uma nova manifestação e adicioná-la ao banco de dados.
    Exibe o código da manifestação cadastrada.
    :param conexao: Conexao do banco de dados
    :param nota: Avaliacao da manifestacao
    :param tipo: Tipo da manifestacao a ser criada
    :param manifestacao: Descricao da manifestacao
    :return: String formatada mostrando o codigo da manifestacao e uma mensagem diferente depedendo da nota
    """
    dados = [nota, tipo, manifestacao]

    inserir_manifestacao = "insert into manifestacoes (avaliacao, tipo, descricao_manifestacao) values (%s, %s, %s)"
    codigo_atual = insertNoBancoDados(conexao, inserir_manifestacao, dados)


    return (f"Manifestacao cadastrada com sucesso. Seu codigo e {codigo_atual} "
            f"{f'\nObrigado pela nota {nota}' if nota >= 3 else 
            '\nLamentamos que sua experiência não tenha sido satisfatória. '
            'Seu feedback é muito importante para melhorarmos nossos serviços.'}")

def atualizar_quantidade(conexao):
    """
    Atualiza a quantidade de manifestacoes
    :param conexao: Conexao do banco de dados
    :return: quantidade de manifestacoes
    """
    quantidade_de_manifestacoes = listarBancoDados(conexao, "select count(*) from manifestacoes")
    if quantidade_de_manifestacoes != "":
        return quantidade_de_manifestacoes[0][0]
    else:
        return 0

def atualizar_codigos(conexao):
    """
    Atualiza a lista de codigos disponiveis
    :param conexao: Conexao do banco de dados
    :return: lista de codigos disponiveis
    """
    codigos_das_manifestacoes = listarBancoDados(conexao, "select codigo from manifestacoes")
    if codigos_das_manifestacoes != "":
        return [codigo[0] for codigo in codigos_das_manifestacoes]
    else:
        return ["Nao ha manifestacoes a serem pesquisadas"]

def exibir_quantidade_manifestacoes(conexao):
    """
    Exibe a quantidade total de manifestações cadastradas.
    """
    quantidade = atualizar_quantidade(conexao)
    return f"Quantidade de manifestacoes cadastradas: {quantidade}"

def pesquisar_manifestacao(conexao, codigo):
    """
    Permite ao usuário pesquisar uma manifestação pelo código.
    Se o código for inválido, informa o erro.
    :param conexao: Conexao do banco de dados
    :param codigo: Codigo para pesquisar a manifestacao
    :return: string formatada com a manifestacao pesquisada
    """
    manifestacao_pesquisada = []
    codigos_manifestacoes_disponiveis = atualizar_codigos(conexao)

    if  codigo not in codigos_manifestacoes_disponiveis or codigo < 0:
        return ["\033[31;1mCodigo pesquisado invalido\033[m"]

    else:

        sql_manifestacao = "select * from manifestacoes where codigo = %s"
        codigo_pesquisado = listarBancoDados(conexao,sql_manifestacao, (codigo, ))


        for codigo, avaliacao, tipo, descricao_manifestacao, data in codigo_pesquisado:
            manifestacao_pesquisada.append("-" * 30 + f"\nCodigo: {codigo}.\n"
                                            f"Nota {avaliacao}.\nTipo da manifestacao: {tipo}\n"
                                            f"{descricao_manifestacao}\n" +
                                            f"Criada em {data}\n" + "-" * 30)

        return manifestacao_pesquisada

def excluir_manifestacao(conexao, codigo):
    """
    Exclui uma manifestacao do banco de dados
    :param conexao: Conexao do banco de dados
    :param codigo: Codigo da manifestacao a ser excluida
    :return: Se foi possivel excluir ou nao
    """
    quantidade = atualizar_codigos(conexao)

    if quantidade == 0:
        return "Nao ha manifestacoes para excluir"

    manifestacao_para_excluir = listarBancoDados(conexao, "Select * from manifestacoes where codigo = %s",
                                                     (codigo, ))
    if not manifestacao_para_excluir:
        return "\033[31;1mCodigo nao encontrado\033[m"

    manifestacao_para_excluir = manifestacao_para_excluir[0]

    sql_excluir = "delete from manifestacoes where codigo = %s"
    exclusao = excluirBancoDados(conexao, sql_excluir, (codigo, ))

    if exclusao > 0:
        return (f"Manifestacao: Codigo {manifestacao_para_excluir[0]}. Nota {manifestacao_para_excluir[1]}. Tipo da "
                f"manifestacao: {manifestacao_para_excluir[2]}\n {manifestacao_para_excluir[3]}\n Excluida com sucesso")
    else:
        return "\033[31;1mErro ao excluir manifestacao\033[m"

# Funcoes para o programa principal da ouvidoria:

def cancelar_operacao(valor):
    """
    Possibilita cancelar uma operacao
    :param valor: Valor para cancelar
    :return: True ou False para cancelar
    """
    if valor is None:
        print("\033[33mOperação cancelada.\033[m")
        return True

    return False

def listagem_das_manifestacoes(lista):
    """
    Print formatado de uma lista
    """
    for manifestacao in lista:
        print(manifestacao)
        sleep(0.5)

def validar_inteiro(texto, minimo, maximo):
    """
    Valida um numero inteiro
    :param texto: Texto para ser exibido ao pedir entrada do usuario
    :param minimo: minimo permitido
    :param maximo: Maximo permitido
    :return: Valor verificado
    """
    print(f"Digite {maximo + 1} para cancelar")
    while True:
        try:
            inteiro = int(input(texto))

            if inteiro == maximo + 1:
                return None

            if minimo <= inteiro <= maximo:
                return inteiro

            else:
                print(f"\033[31;1mDigite um valor entre {minimo} e {maximo + 1}\033[m")

        except ValueError:
            print("\033[31;1mERRO. Digite um numero valido\033[m")

def validar_tipo_manifestacao():
    """
    Valida o tipo de manifestacao
    :return: Tipo verificado
    """
    tipo = validar_inteiro("1 - Sugestão\n2 - Reclamação\n3 - Elogio \nDigite o numero: ", 1, 3)
    tipos_de_manifestacoes = ["Sugestao", "Elogio", "Reclamacao"]

    return tipo


def validar_codigo_da_manifestacao():
    """
    Verifica se o codigo da manifestacao e possibilita cancelar a operacao
    :return:
    """
    codigos_manifestacoes_disponiveis = atualizar_codigos(conexao)
    while True:
        print("Digite 0 para cancelar")
        try:
            codigo = int(input("Digite o codigo da manisfetacao: "))

            if codigo == 0:
                return None

            elif codigo > 0 and codigo in codigos_manifestacoes_disponiveis:
                return codigo

            else:
                print("\033[31;1mCódigo inválido!\033[m")

        except ValueError:
            print("\033[31;1mDigite um codigo valido!\033[m")