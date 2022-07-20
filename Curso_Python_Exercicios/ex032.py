ano = int(input("Digite um ano: "))

if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print("{} foi, é ou será um ano bissexto.".format(ano))
else:
    print("{} não foi, é ou será um ano bissexto.".format(ano))
