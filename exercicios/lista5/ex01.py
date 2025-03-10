# •1) Crie um metodo que receba um valor em reais e converta a dólares

def realParaDolar(valor):
    valorEmDolar = valor / 5.83
    valorEmDolar = round(valorEmDolar, 2)
    return (valorEmDolar)

real = 50
print(realParaDolar(real))
