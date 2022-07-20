qtdElementos = int(input("Digite o número de elementos da sequência de Fibonacci que você deseja ver: "))
nElementos = 1
elemento1 = 0
elemento2 = 1

while nElementos <= qtdElementos:
    novoElemento = elemento1 + elemento2
    print(elemento1, end=" -> ")
    elemento1 = elemento2
    elemento2 = novoElemento
    nElementos = nElementos + 1
print("Fim")
