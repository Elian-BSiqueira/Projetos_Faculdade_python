''''• 9) Crie um metodo que receba o valor do salario e indique a quantidade de imposto a ser pago (se ganhar até 2000,
12%. Acima de 2000, 25%) '''

def impostoAPagar(salario):
    if 0 <= salario <= 2000:
        taxaImposto = 12

    elif salario > 2000:
        taxaImposto = 25

    imposto = salario * (taxaImposto / 100)

    return f"Imposto a ser pago com salario de R${salario} a uma taxa de {taxaImposto}% equivale a R${imposto}"

print(impostoAPagar(2500))
