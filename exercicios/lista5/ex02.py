''' • 2) Crie um metodo que receba 2 parâmetros: um valor em reais e a moeda que deve ser convertida (dólares, euros
ou peso argentino). E realize a conversão'''

def conversorMoedasReal(valor, moeda):
    moeda = moeda.strip().lower()
    if moeda == "dolar":
        valorConvertido = valor / 5.83

    elif moeda == "euro":
        valorConvertido = valor * 0.16

    elif moeda == "peso argentino":
        valorConvertido = valor * 181.97

    valorConvertido = round(valorConvertido, 2)
    return (valorConvertido)

print(conversorMoedasReal(5, "peso argentino"))