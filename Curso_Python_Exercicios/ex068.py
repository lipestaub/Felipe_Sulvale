from random import randint
from time import sleep

Nvitorias = 0
while True:
    numeroPC = randint(0, 10)
    numeroJogador = int(input("Digite um número: "))
    while numeroJogador > 10 or numeroJogador < 0:
        print("Número inválido!")
        numeroJogador = int(input("Digite um número: "))
    escolhaJogador = input("Par ou Ímpar? (P/I): ").upper().strip()
    while escolhaJogador != "P" and escolhaJogador != "I":
        print("Escolha inválida!")
        escolhaJogador = input("Par ou Ímpar? (P/I): ").upper().strip()
    somaNumeros = numeroPC + numeroJogador
    sleep(1)
    print(f"Você escolheu {numeroJogador} e o computador escolheu {numeroPC}. A soma foi igual a {somaNumeros}!")
    if (somaNumeros % 2) == 0:
        sleep(1)
        print("Deu par!!")
        resultado = "P"
    else:
        sleep(1)
        print("Deu ímpar!!")
        resultado = "I"
    if resultado == escolhaJogador:
        sleep(1)
        print("Você venceu!\nVamos jogar novamente...")
        sleep(1)
        Nvitorias += 1
    else:
        sleep(1)
        print(f"Você perdeu!\nGAME OVER! Você venceu {Nvitorias} vez(es).")
        break
