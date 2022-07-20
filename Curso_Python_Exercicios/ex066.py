somaNumerosDigitados = 0
qtdNumerosDigitados = 0
while True:
    numeroUsuario = int(input("* Digite '999' se deseja ver os resultados! *\nDigite um número: "))
    if numeroUsuario == 999:
        break
    somaNumerosDigitados = somaNumerosDigitados + numeroUsuario
    qtdNumerosDigitados = qtdNumerosDigitados + 1
print(f"Você digitou {qtdNumerosDigitados} números! O resultado da soma entre eles é igual a: {somaNumerosDigitados}")
