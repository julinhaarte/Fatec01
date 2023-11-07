from random import randint

lista = [0]*7

for _ in range(6000):
    n = randint(1,6)
    lista[n] = lista[n]+1

p = [0]*7
for i in range(1, 7):
    p[i] = (lista[i] / 6000)*100
    print(f"O número {i} | Foi sorteado {p[i]:.2f}% das vezes, sendo sorteado {lista[i]} vezes.")
