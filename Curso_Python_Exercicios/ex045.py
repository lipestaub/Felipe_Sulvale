from random import randint
from time import sleep

jogarNovamente = 1


class VerificarEntradaNovoJogo:
    def __init__(self, jogarNovamente):

        self.jogarNovamente = int(jogarNovamente)

        if self.jogarNovamente == 0:
            print("Bom jogo! Até a próxima")
        elif self.jogarNovamente != 0 and self.jogarNovamente != 1:
            print("Informe um valor válido!")
            print("-" * 15)
            sleep(2)
            jogarNovamente = int(input("0 - Não\n1 - Sim\nDeseja jogar novamente? "))

            self.jogarNovamente = VerificarEntradaNovoJogo(jogarNovamente).jogarNovamente


class MostrarEscolhaComputador:
    def __init__(self, escolhaPC):

        self.escolhaPC = int(escolhaPC)

        if self.escolhaPC == 1:
            self.escolha = "Pedra!"
        elif self.escolhaPC == 2:
            self.escolha = "Papel!"
        else:
            self.escolha = "Tesoura!"


class VerificarEntradaUsuario:
    def __init__(self, escolhaJogador):

        self.escolhaJogador = int(escolhaJogador)

        if self.escolhaJogador != 1 and self.escolhaJogador != 2 and self.escolhaJogador != 3:
            print("Informe um valor válido!")
            print("-"*15)
            sleep(2)
            escolhaJogador = int(input("1 - Pedra\n2 - Papel\n3 - Tesoura\nFaça sua escolha: "))

            VerificarEntradaUsuario(escolhaJogador)


class VerificarVencedor:
    def __init__(self, escolhaPC, escolhaJogador):

        self.escolhaPC = int(escolhaPC)
        self.escolhaJogador = int(escolhaJogador)

        if self.escolhaPC == 1 and self.escolhaJogador == 3:
            self.frase = "Você perdeu! Pedra vence Tesoura."
        elif self.escolhaPC == 2 and self.escolhaJogador == 1:
            self.frase = "Você perdeu! Papel vence Pedra."
        elif self.escolhaPC == 3 and self.escolhaJogador == 2:
            self.frase = "Você perdeu! Tesoura vence Papel."
        elif self.escolhaJogador == 1 and self.escolhaPC == 3:
            self.frase = "Você venceu! Pedra vence Tesoura."
        elif self.escolhaJogador == 2 and self.escolhaPC == 1:
            self.frase = "Você venceu! Papel vence Pedra."
        elif self.escolhaJogador == 3 and self.escolhaPC == 2:
            self.frase = "Você venceu! Tesoura vence Papel."
        else:
            self.frase = "Empate"


while jogarNovamente != 0:

    escolhaPC = randint(1, 3)

    escolhaJogador = int(input("1 - Pedra\n2 - Papel\n3 - Tesoura\nFaça sua escolha: "))

    VerificarEntradaUsuario(escolhaJogador)

    print("Eu escolho...")

    sleep(1)

    print("Processando...")

    sleep(2)

    print(MostrarEscolhaComputador(escolhaPC).escolha)

    sleep(2)

    print(VerificarVencedor(escolhaPC, escolhaJogador).frase)
    sleep(1)

    jogarNovamente = int(input("0 - Não\n1 - Sim\nDeseja jogar novamente? "))

    jogarNovamente = VerificarEntradaNovoJogo(jogarNovamente).jogarNovamente
