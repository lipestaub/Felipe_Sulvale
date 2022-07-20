print("-=-=-=-=- PROGRESSÃO ARITMÉTICA -=-=-=-=-")

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

contador = 1

while contador <= 10:
    print(termo, end=" -> ")
    termo += razao
    contador += 1

print("Fim")
