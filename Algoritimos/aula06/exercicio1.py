print("Vamos verificar se um número é divisível por 3 e 5 simultâneamente?")
a = int(input("Insira um número:"))

if a % 5 == 0 and a % 3 == 0:
    print(f"Que legal! {a} é divisível por 3 e 5! :)")
else:
    print(f"Que pena! {a} não é divisível por 3 e 5! :(")
