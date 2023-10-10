vetor = []

for i in range(5):
    vetor.append(int(input(f"Digite o número {i+1}:")))

pos = 0
maior = vetor[pos]

for i  in range(0, len(vetor)):
    if vetor[i] >= maior:
        maior = vetor[i]
        pos = i

print(f"O maior número é: {maior} na posição: {pos}")