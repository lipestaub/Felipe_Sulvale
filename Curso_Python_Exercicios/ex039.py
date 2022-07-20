from datetime import date
from time import sleep


class ValidarSexo:
    def __init__(self, sexo):
        self.sexoUsuario = int(sexo)

        if self.sexoUsuario != 1 and self.sexoUsuario != 2:
            print("Informe um valor válido\n" + "-"*20)
            sleep(2)
            self.sexoUsuario = int(input("- 1 -> Masculino\n- 2 -> Feminino\nInforme seu sexo: "))

            ValidarSexo(self.sexoUsuario)


anoAtual = date.today().year

anoNascimento = int(input("Em que você nasceu? "))

idade = anoAtual-anoNascimento
sexoUsuario = int(input("- 1 -> Masculino\n- 2 -> Feminino\nInforme seu sexo: "))

sexoUsuario = ValidarSexo(sexoUsuario).sexoUsuario

if sexoUsuario == 1:
    if idade < 18:
        print("Você deverá se alistar em {}. Faltam {} ano(s)!".format(anoNascimento+18, (anoNascimento+18)-anoAtual))
    elif idade == 18:
        print("Você completa 18 anos neste ano. Está na hora de se alistar!")
    else:
        print("Você deveria ter se alistado em {}! Há {} ano(s) atrás.".format(anoNascimento+18,
                                                                               anoAtual-(anoNascimento+18)))
else:
    print("O serviço militar não é obrigatório para as mulheres.")
