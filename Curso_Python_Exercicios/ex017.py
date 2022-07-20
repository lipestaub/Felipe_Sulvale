from math import sqrt, pow

cateto1 = float(input("Digite o valor do cateto oposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))

print("O valor da hipotenusa é: {:.2f}".format(sqrt(pow(cateto1, 2)+pow(cateto2, 2))))