lista = []

for i in range(5):
    lista.append(int(input(f"Digite o número {i+1}:")))

for i in lista[::-1]:
    print(i, end=' ')

print()
print(lista)
