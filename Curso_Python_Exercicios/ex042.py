reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    if reta1 == reta2 == reta3:
            tipoTriangulo = "EQUILÁTERO"
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipoTriangulo = "ISÓSCELES"
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        tipoTriangulo  = "ESCALENO"

    print("As retas de comprimento {}, {} e {} PODEM formar um triângulo {}!".format(reta1, reta2, reta3, tipoTriangulo))
else:
    print("As retas de comprimento {}, {} e {} NÃO PODEM formar um triângulo!".format(reta1, reta2, reta3))