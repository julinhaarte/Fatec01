frase = input("Digite a frase: ")
palavra = input("Digite a palavra: ")

qtd = frase.count(palavra)
total_palavras = frase.count(' ') + 1

print(f"A frase possuí um total de {total_palavras} palavras.")
print(f"A palavra {palavra} aparece {qtd} vezes na frase.")
