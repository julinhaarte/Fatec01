n = int(input(f"Insira o número que será potencionado:"))
e = 0
for i in range(1,n+1):
    e = e + (2**i)
print(f"O valor de e: {e}")
