'''• Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

listaDeNumeros = []
while True:
    print("=" * 30)
    while True:
        try:
            quantidadeDeNumeros = int(input("Quantos numeros quer adicionar ao conjunto? "))
            if quantidadeDeNumeros > 0:
                break
            else:
                print("Digite um numero maior que 0")
        except ValueError:
            print("Digite apenas numeros inteiros")

    contador = 1
    for n in range(1, quantidadeDeNumeros + 1):
        while True:
            try:
                numero = int(input(f"Digite o {contador} numero: "))
                if numero >= 0:
                    contador += 1
                    listaDeNumeros.append(numero)
                    break
                else:
                    print("Digite um numero maior que 0")
            except ValueError:
                print("Digite apenas numeros inteiros")

    print("=" * 30)
    opcao = input("Deseja adicionar mais numeros [S / N]? ").upper().strip()
    print("=" * 30)
    while opcao not in "SN":
        print("Digite apenas 'S' ou 'N'")
        opcao = input("Deseja adicionar mais numeros [S / N]? ").upper().strip()

    if opcao == "S":
        continue

    else:
        break

print("Numeros informados: ")
soma = sum(listaDeNumeros)
for numero in listaDeNumeros:
    print(numero, end=" ")

print("=" * 30)
print(f"\nO maior numero informado foi {max(listaDeNumeros)}")
print(f"O menor numero informado foi {min(listaDeNumeros)}")
print(f"A soma de todos os numeros informados e {soma}")



