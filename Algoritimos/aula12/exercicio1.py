d = {}

for i in range(5):
    snome = input("Insira o sobrenome:")
    idade = int(input("Insira a idade:"))
    d[snome] = idade

maior_sobrenome = ""
maior_idade = 0

for chave, valor in d.items():
    if valor > maior_idade:
        maior_idade = valor
        maior_sobrenome = chave

print(f"O sobrenome com maior idade é {maior_sobrenome}")
