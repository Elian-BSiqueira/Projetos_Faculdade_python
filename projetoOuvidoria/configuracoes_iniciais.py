from funcoes_mysql import *
from config import *

conexao = criarConexao(host, user, password, database)
quantidade_de_manifestacoes = listarBancoDados(conexao, "select count(*) from manifestacoes")
quantidade_de_manifestacoes = quantidade_de_manifestacoes[0][0]

codigos_de_manifestacoes = listarBancoDados(conexao, "select codigo from manifestacoes")
codigos_filmes_disponiveis = []

for codigo in codigos_de_manifestacoes:
    code = codigo[0]
    codigos_filmes_disponiveis.append(code)
