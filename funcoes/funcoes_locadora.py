from time import sleep
from funcoes.funcoes_mysql import *
from Locadora.config import *

conexao = criarConexao(host, user, password, database)
quantidade_de_filmes = listarBancoDados(conexao, 'select count(*) from filmes')
quantidade_de_filmes = quantidade_de_filmes[0][0]
codigos_de_filmes = listarBancoDados(conexao, "select codigo from filmes")
codigos_filmes_disponiveis = []
for codigo in codigos_de_filmes:
    code = codigo[0]
    codigos_filmes_disponiveis.append(code)




def exibirmenu():
    # Exibe o menu do programa

    return ("=" * 30 + "\n" +
            "Locadora".center(28) + "\n" +
            "=" * 30 + "\n" +
            'Opcao 1 - Listar filmes\n'
            'Opcao 2 - Alugar filme\n'
            'Opcao 3 - Adicionar filme\n'
            'Opcao 4 - Sair'
            )

def listarfilmes(conexao):
    # Lista os filmes disponiveis para algugar
    listar_filmes = listarBancoDados(conexao, 'select * from filmes')

    if not listar_filmes:
        return ['Nenhum filme disponível no momento.']

    else:
        mensagem = ['Filmes disponíveis:']

        for codigo, nome, sinopse, ano in listar_filmes:
            mensagem.append(f"{codigo}: 🎬 {nome} ({ano})\n📖 Sinopse: {sinopse}\n{'-' * 50}")

    return mensagem

def alugarfilme(conexao, numeroDoFilmeEscolhido):
    # Permine o usuario alugar um filmes
    listar_filmes = listarBancoDados(conexao, 'select codigo, nome from filmes')


    sleep(0.5)
    if quantidade_de_filmes == 0:
        return 'Nenhum filme disponivel'


    filmeAlugado = numeroDoFilmeEscolhido
    filme = listarBancoDados(conexao, "select * from filmes where codigo = %s", (numeroDoFilmeEscolhido, ))
    excluirBancoDados(conexao, 'delete from filmes where codigo = %s', (numeroDoFilmeEscolhido, ))

    return f'filme {filme[0][1]} alugado com sucesso'


def adicionarFilme(conexao, dados):
    # Permite o usuario adicionar um filme para alugar
    inserir_filme = 'insert into filmes (nome, sinopse, ano) values (%s, %s, %s)'


    insertNoBancoDados(conexao, inserir_filme, dados)
    return f"Filme {dados[0]} adicionado com sucesso"

