from funcoes_mysql import *
from config import *

conexao = criarConexao(host, user, password, database)
quantidade_de_manifestacoes = listarBancoDados(conexao, "select count(*) from manifestacoes")
quantidade_de_manifestacoes = quantidade_de_manifestacoes[0][0]

def exibir_menu():
    """
    Exibe o menu de opções do sistema para o usuário.
    """
    return ("=" * 40 + "\n" +
            "1) Listagem das Manifestações\n"
            "2) Criar uma nova Manifestação\n"
            "3) Exibir quantidade de manifestações\n"
            "4) Pesquisar uma manifestação por código\n"
            "5) Sair do Sistema\n" +
            "=" * 40)

def listar_manifestacoes(conexao):
    """
    Lista todas as manifestações cadastradas.
    Se não houver manifestações, informa ao usuário.
    """
    sql_listagem = "select codigo, avaliacao, descricao_manifestacao from manifestacoes"
    lista_de_manifestacoes = listarBancoDados(conexao, sql_listagem)

    manifestacoes = []

    if not lista_de_manifestacoes:
        manifestacoes.append("Nao ha manifestacoes")
        return manifestacoes

    else:
        for codigo, avaliacao, descricao_manifestacao in lista_de_manifestacoes:
            manifestacoes.append(f"{codigo}. Nota {avaliacao}\n {descricao_manifestacao}\n" + "-" * 30)

        return manifestacoes

def criar_manifestacao(conexao, nota, manifestacao):
    """
    Permite ao usuário criar uma nova manifestação e adicioná-la à lista.
    Exibe o código da manifestação cadastrada.
    """
    dados = [nota, manifestacao]

    inserir_manifestacao = "insert into manifestacoes (avaliacao, descricao_manifestacao) values (%s, %s)"
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
    """
    if  codigo > quantidade_de_manifestacoes or codigo < 0:
        return "\033[31;1mCodigo pesquisado invalido\033[m"

    else:

        sql_manifestacao = "select * from manifestacoes where codigo = %s"
        manifestacao_pesquisada = listarBancoDados(conexao,sql_manifestacao, (codigo, ))

        return manifestacao_pesquisada




