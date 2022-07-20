from random import randint

Nsorteado = randint(0, 5)

Nusuario = int(input("Digite um número entre 0 e 5: "))

if Nsorteado == Nusuario:
    print("Parabéns! Você venceu.")
else:
    print("Você perdeu. O número correto era o: {}".format(Nsorteado))
