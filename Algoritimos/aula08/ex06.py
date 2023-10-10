palavra = input("Digite a palavra:")
inverso_palavra = palavra[::-1]
if palavra.lower() == inverso_palavra.lower():
    print(f"A palavra {palavra}")