primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

if primeiroNumero > segundoNumero:
    print("O primeiro valor ({}) é maior que o segundo valor ({}).".format(primeiroNumero, segundoNumero))
elif segundoNumero > primeiroNumero:
    print("O segundo valor ({}) é maior que o primeiro valor ({}).".format(segundoNumero, primeiroNumero))
else:
    print("Os valores são iguais.".format(primeiroNumero, segundoNumero))