sal = float(input("Insira seu salário atual: R$"))
aumento = float(input("Insira a porcentagem de aumento:"))
sal_atual = sal + (sal*aumento/100)
print(f"Seu salário reajustado é: R${sal_atual:.2f}")
