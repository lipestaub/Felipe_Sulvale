contador = 1
while True:
    entradaUsuario = int(input("Digite um número: "))
    if entradaUsuario < 0:
        break
    while contador <= 10:
        print(f"{entradaUsuario} x {contador} = {entradaUsuario*contador}")
        contador += 1
    contador = 1
    print("-" * 20)
print("Programa encerrado.")
