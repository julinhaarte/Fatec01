from math import pi

def volume(raio):

    volume = (4/3) * pi * raio**3
    return volume

raio = float(input("Digite o raio da esfera: "))

volume_esfera = volume(raio)

# Exibir o resultado
print(f"O volume da esfera com raio {raio} é aproximadamente {volume_esfera:.2f}m³.")
