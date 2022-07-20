from random import randint
from time import sleep


def getNumeroUsuario():
    entradaUsuario = int(input("Digite um número entre 0 e 10: "))
    return entradaUsuario


contadorTentativas = 1

numeroPC = randint(0, 10)
numeroUsuario = getNumeroUsuario()

while numeroUsuario != numeroPC:

    if numeroUsuario != numeroPC:
        print("Você errou!")
        if numeroUsuario > numeroPC:
            print("Menos... tente outra vez!")
        elif numeroUsuario < numeroPC:
            print("Mais... tente outra vez!")
        contadorTentativas = contadorTentativas + 1
        sleep(0.75)
        numeroUsuario = getNumeroUsuario()

print("PARABÉNS! Você acertou na sua {}ª tentativa.".format(contadorTentativas))
