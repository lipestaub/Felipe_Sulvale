maiorNumero = 0
menorNumero = 0

qtdNumerosDigitados = 0
somaNumerosDigitados = 0

continuar = 1

while continuar == 1:
    numeroUsuario = int(input("Digite um número: "))

    if qtdNumerosDigitados == 0:
        maiorNumero = numeroUsuario
        menorNumero = numeroUsuario
    else:
        if numeroUsuario > maiorNumero:
            maiorNumero = numeroUsuario
        elif numeroUsuario < menorNumero:
            menorNumero = numeroUsuario

    qtdNumerosDigitados = qtdNumerosDigitados + 1
    somaNumerosDigitados = somaNumerosDigitados + numeroUsuario

    continuar = int(input("1 -> SIM\n2 -> NÃO\nDeseja continuar? "))

    while continuar != 1 and continuar != 2:
        print("Entrada inválida!")
        continuar = int(input("1 -> SIM\n2 -> NÃO\nDeseja continuar? "))

media = somaNumerosDigitados / qtdNumerosDigitados

print("O maior valor digitado foi {}, e o menor foi {}! A média entre os valores foi {:.2f}".format(maiorNumero,
                                                                                                    menorNumero, media))
