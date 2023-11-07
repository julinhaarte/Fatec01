def converter_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))


segundos_totais = converter_segundos(horas, minutos, segundos)


print(f"{horas} horas, {minutos} minutos e {segundos} segundos correspondem a {segundos_totais} segundos.")