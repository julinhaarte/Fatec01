def calcular_soma_multiplicacao(numero_str):
    soma = 0
    multiplicacao = 1

    for digito_str in numero_str:
        digito = int(digito_str)
        soma += digito
        multiplicacao *= digito

    return soma, multiplicacao

ra = "3011392323027"
soma, multiplicacao = calcular_soma_multiplicacao(ra)

print(f"Soma = {soma}")
print(f"Multiplicação = {multiplicacao}")