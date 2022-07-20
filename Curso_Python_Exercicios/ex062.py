from time import sleep

print("-=-=-=-=- PROGRESSÃO ARITMÉTICA -=-=-=-=-")

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
qtdTermosExibidos = 0

while contador <= 10:
    print(termo, end=" -> ")
    termo += razao
    contador += 1
    qtdTermosExibidos += 1
print("Fim")

contador = 1

qtdTermos = None

while qtdTermos != 0:
    sleep(1.25)
    qtdTermos = int(input("Deseja mostrar mais quantos termos? "))
    if qtdTermos != 0:
        while contador <= qtdTermos:
            print(termo, end=" -> ")
            termo += razao
            contador += 1
            qtdTermosExibidos += 1
        print("Fim")
        contador = 1
    else:
        print("Foram exibidos {} termos. Até a próxima!".format(qtdTermosExibidos))
        sleep(1.5)
