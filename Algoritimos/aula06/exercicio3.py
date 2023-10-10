print("Vamos calcular quantos litros de tinta serão necessários para pintar o cômodo!")
comprimento = float(input("Insira a comprimento da parede em metros:"))
largura = float(input("Insira a largura da parede em metros:"))
area = ((comprimento*2.80)*2 + (largura*2.80)*2)-0.80*2.10
litro = area/3
lata = (area/3)/18
galao = (area/3)/36

print(f"A área a ser pintada é igual a: {area:.2f} metros quadrados.")
print(f"Dessa forma, você precisará de: {area/3:.2f} litros de tinta.")

if 18 <= litro < 36:
    print(f"O que equivale a: {lata:.1f} latas de tinta")

elif litro >= 36:
    print(f"O que equivale a: {galao:.1f} galões de tinta")


print(f"Mãos à obra! Espero que dê tudo certo com a sua pintura!")
