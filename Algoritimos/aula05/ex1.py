nota1 = float(input("Insira a nota 1:"))
nota2 = float(input("Insira a nora 2:"))
nota3 = float(input("Insira a nota 3:"))
nota_exame = 0
media = (nota1 + nota2 + nota3) / 3

if media < 3.0:
    resultado = "Você está reprovado(a)! :("

else:
    if media < 7.0:
        resultado = "Você está de exame! :o"
    else:
        resultado = "Parabéns! Você está aprovado(a)! :D"

print(f"Média:{media:5.2f} - {resultado}")
