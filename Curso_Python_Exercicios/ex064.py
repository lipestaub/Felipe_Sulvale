numeroUsuario = None

somaNumerosDigitados = 0
qtdNumerosDigitados = 0

while numeroUsuario != 999:
    numeroUsuario = int(input("* Digite '999' se deseja ver os resultados! *\nDigite um número: "))

    if numeroUsuario != 999:
        somaNumerosDigitados = somaNumerosDigitados + numeroUsuario
        qtdNumerosDigitados = qtdNumerosDigitados + 1

print("Você digitou {} números! O resultado da soma entre eles é igual a: {}".format(qtdNumerosDigitados,
                                                                                     somaNumerosDigitados))
