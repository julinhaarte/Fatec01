def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return 1
    else:
        return 0

ano = int(input("Digite o ano (formato AAAA): "))

resultado = ano_bissexto(ano)

if resultado == 1:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")