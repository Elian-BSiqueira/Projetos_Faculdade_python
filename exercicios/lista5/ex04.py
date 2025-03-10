# • 4) Crie um metodo que receba o peso e altura e retorne o IMC.

def calculoIMC(peso, altura):
    altura /= 100
    imc = peso / altura ** 2
    imc = round(imc, 2)
    return imc

print(calculoIMC(90, 180))


