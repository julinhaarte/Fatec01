

nasc = int(input("Insira sua data de nascimento:"))
ano = int(input("Insira o ano em que estamos:"))
idade = ano-nasc
idade_meses = idade*12
idade_dias = idade*365
idade_semanas = idade*53

print("Você tem:", idade, "anos,", idade_meses, "meses,", idade_semanas, "semanas e", idade_dias, "dias!")
print("Sua idade em anos é:", idade)
print("Sua idade em meses é:", idade_meses)
print("Sua idade em semanas é:", idade_semanas)
print("Sua idade em dias é:", idade_dias)
