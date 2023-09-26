a = int(input(f"Insira a quantidade de idades:"))
soma = 0
for i in range(1,(a+1)):
    n = int(input(f"Entre com a {i}a idade: "))
    soma = soma + n
media = soma / (a)
print(f"A média das idades é {media:5.2f}")

