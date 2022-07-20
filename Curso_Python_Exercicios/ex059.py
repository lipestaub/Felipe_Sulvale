from time import sleep

def exibirMenu():
    print("1 -> somar\n2 -> multiplicar\n3 -> descobrir qual é o maior valor\n4 -> digitar novos números\n5 -> sair "
          "do programa")


def verificarEntradaOperacao(entradaUsuario):
    if entradaUsuario != 1 and entradaUsuario != 2 and entradaUsuario != 3 and entradaUsuario != 4 and entradaUsuario != 5:
        print("Entrada inválida!")
        sleep(2)
        exibirMenu()
        entradaUsuario = int(input("O que você deseja fazer: "))
        verificarEntradaOperacao(entradaUsuario)

    return entradaUsuario


def somar(a, b):
    resultado = a + b

    return resultado


def multiplicar(a, b):
    resultado = a * b

    return resultado


def retornarMaiorValor(a, b):
    if a > b:
        resultado = a
    elif b > a:
        resultado = b
    else:
        resultado = 0

    return resultado


operacao = None

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

while operacao != 5:
    exibirMenu()
    operacao = verificarEntradaOperacao(int(input("O que você deseja fazer: ")))

    if operacao == 1:
        print("O resultado da soma entre os valores é {:.2f}".format(somar(valor1, valor2)))
        sleep(2)
    elif operacao == 2:
        print("O resultado da multiplicação entre os valores é {:.2f}".format(multiplicar(valor1, valor2)))
        sleep(2)
    elif operacao == 3:
        if retornarMaiorValor(valor1, valor2) == 0:
            print("Os valores são iguais")
        else:
            print("O maior valor digitado foi {}".format(retornarMaiorValor(valor1, valor2)))
        sleep(2)
    elif operacao == 4:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
