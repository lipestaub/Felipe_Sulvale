def InverterFrase(frase):
    fraseInvertida = frase.replace(' ', '')[::-1]

    return fraseInvertida


fraseUsuario = input("Digite uma frase: ")

if fraseUsuario.replace(' ', '') == InverterFrase(fraseUsuario):
    print("A frase '{}' é um palíndromo!".format(fraseUsuario))
else:
    print("A frase '{}' não é um palíndromo!".format(fraseUsuario))
