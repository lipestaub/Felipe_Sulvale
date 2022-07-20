from math import factorial
from time import sleep

valor = int(input("Digite um número inteiro: "))

resultadoFatorial = factorial(valor)

print("{}! = ".format(valor), end="")

while valor > 0:
    if valor > 1:
        print(valor, end="x")
    else:
        print(valor)
    valor -= 1

sleep(1)
print("Resultado = {}".format(resultadoFatorial))
