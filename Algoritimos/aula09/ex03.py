lista = []

for i in range(5):
    lista.append(int(input(f"Digite o número {i+1}:")))

maior = sorted(lista, reverse=True)[0]
pos = lista.index(maior)

print(f"O maior número é: {maior} na posição: {pos}")