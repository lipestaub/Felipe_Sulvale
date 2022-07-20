maiorPeso = 0
menorPeso = 0

for i in range(1, 6):
    peso = int(input("Digite o peso da {}ª pessoa: ".format(i)))

    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

print("O maior peso foi igual a {} kg e o menor peso foi igual a {} kg!".format(maiorPeso, menorPeso))
