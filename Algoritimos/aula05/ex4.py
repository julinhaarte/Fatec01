zEdia = int(input("Insira o número do dia:"))

match dia:
    case 1:
        nome = "Domingo"
    case 2:
        nome = "Segunda-feira"
    case 3:
        nome = "Terça-feira"
    case 4:
        nome = "Quarta-feira"
    case 5:
        nome = "Quinta-feira"
    case 6:
        nome = "Sexta-feira"
    case 7:
        nome = "Sábado"
    case _:
        nome = f"O valor {dia} é inválido!"

print(nome)
