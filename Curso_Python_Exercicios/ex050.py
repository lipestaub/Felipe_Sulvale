soma = 0
qtdPares = 0

for i in range(0, 6):
    entradaUsuario = int(input("Digite um número inteiro: "))

    if (entradaUsuario % 2) == 0:
        soma += entradaUsuario
        qtdPares = qtdPares + 1

print("A soma dos {} números pares digitados é igual a: {}".format(qtdPares, soma))
