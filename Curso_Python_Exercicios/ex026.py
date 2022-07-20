frase = input("Digite uma frase: ").strip()

qtdA = frase.replace(' ', '').upper().count('A')
primeiroA = frase.upper().find('A')
ultimoA = frase.upper().rfind('A')

print("A letra a aparece {} ves(es)".format(qtdA))
print("A primeira letra a aparece na posição {}".format(primeiroA+1))
print("A última letra a aparece na posição {}".format(ultimoA+1))
