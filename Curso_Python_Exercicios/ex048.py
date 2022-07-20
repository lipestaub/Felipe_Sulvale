soma = 0
qtdNumeros = 0

for i in range(1, 500):
    if (i % 2) != 0 and (i % 3) == 0:
        soma += i
        qtdNumeros = qtdNumeros + 1

print("A soma dos {} números ímpares e múltiplos de 3 entre 1 e 500 é igual a: {}  ".format(qtdNumeros, soma))
