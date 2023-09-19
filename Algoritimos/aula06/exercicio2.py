print("Vamos descobrir qual será seu desconto?")
valor = float(input("Qual o valor da sua compra em R$?"))
dez = valor - ((valor*10)/100)
vinte = valor - ((valor*20)/100)
trinta = valor - ((valor*20)/100)
if valor <= 1000.00:
    print(f"Que bacana! Seu desconto será de 10%!")
    print(f"Dessa forma, sua compra ficará em: R${dez:.2f}")

elif 1000.00 < valor <= 5000.00:
    print(f"Que demais! Seu desconto será de 20%!")
    print(f"Dessa forma, sua compra ficará em: R${vinte:.2f}")

elif valor > 5000.00:
    print(f"Que pechincha! Seu desconto será de 30%!")
    print(f"Dessa forma, sua compra ficará em: R${trinta:.2f}")
