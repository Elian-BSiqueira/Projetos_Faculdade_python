'''
• 3) Crie um metodo que receba 3 parâmetros: um valor, moeda de origem e a moeda que deve ser convertida (dolares, euros
 ou peso argentino). E realize a conversão.
'''


def conversorMoedas(valor, moeda_origem="BRL", moeda_conversao="USD"):
    moeda_origem = moeda_origem.strip().upper()
    moeda_conversao = moeda_conversao.strip().upper()

    taxas = {"BRL": {"USD": 0.17, "EUR": 0.16, "ARS": 187.78},
            "USD": {"BRL": 5.7064, "EUR": 0.92, "ARS": 1073.10},
            "EUR": {"BRL": 6.18, "USD": 1.08, "ARS": 1160.72},
            "ARS": {"BRL": 0.0062, "EUR": 0.00097, "USD": 0.0011}
    }

    taxa_de_conversao = taxas[moeda_origem][moeda_conversao]
    moeda_convertida = valor * taxa_de_conversao
    return round(moeda_convertida, 2)

valor = 1000
print(conversorMoedas(valor, "usd", "brl"))