print(f"Dê os lados a, b e c de um triãngulo")
a = int(input("Insira a:"))
b = int(input("Insira b:"))
c = int(input("Insira c:"))

if (a+b) > c or (b+c) < a or (a+c) < b:
    print("É um triângulo!")
else:
    print(f"Esses lados não formam um triângulo. :(")

if a == b == c:
    print(f"O triângulo é equilátero!")
elif a == b != c or a != b == c or a == c != b or b == c != a:
    print(f"triângulo é isóceles!")
elif a != b != c:
    print(f"O triângulo é escaleno!")
