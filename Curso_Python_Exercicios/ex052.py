entradaUsuario = int(input("Digite um número: "))
qtdDivisoesPossiveis = 0

for i in range(1, entradaUsuario + 1):
    if (entradaUsuario % i) == 0:
        qtdDivisoesPossiveis = qtdDivisoesPossiveis + 1

if qtdDivisoesPossiveis <= 2:
    print("O número {} foi divisível {} vez(es). Ele É um número primo!".format(entradaUsuario, qtdDivisoesPossiveis))
else:
    print("O número {} foi divisível {} vez(es). Ele NÃO É um número primo!".format(entradaUsuario,
                                                                                    qtdDivisoesPossiveis))
