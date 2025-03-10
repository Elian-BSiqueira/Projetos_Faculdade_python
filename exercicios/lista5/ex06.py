# • 6) Crie um metodo que receba as notas e retorne a média de notas do aluno

def notasAluno(*quantidadeNotas):
    listaNotas = list(quantidadeNotas)
    soma = 0
    for nota in quantidadeNotas:
        soma += nota
    media = soma / len(listaNotas)
    return media

print(notasAluno(7, 6, 8, 7))
