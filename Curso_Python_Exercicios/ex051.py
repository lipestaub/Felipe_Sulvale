print("-=-=-=-=- PROGRESSÃO ARITMÉTICA -=-=-=-=-")

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
ultimoTermo = primeiroTermo + (9 * razao)

for i in range(primeiroTermo, ultimoTermo + 1, razao):
    print(i, end=" -> ")

print("Fim")
