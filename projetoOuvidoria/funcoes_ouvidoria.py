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


    return f"Manifestacao cadastrada com sucesso. Seu codigo e {codigo_atual}"

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
