# • 5) Crie um metodo que receba as notas e retorne a maior nota do aluno


def notasAluno(*quantidadeNotas):
    listaNotas = list(quantidadeNotas)
    for nota in quantidadeNotas:
        print(nota, end=" ")
    listaNotas.sort(reverse=True)
    return f"\nA maior nota e {listaNotas[0]}"

notas = notasAluno(1, 2, 4, 7, 10, 9)
print(notas)