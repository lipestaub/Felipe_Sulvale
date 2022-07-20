distancia = int(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    print("O valor da passagem é R$ {:.2f}".format(distancia*0.5))
else:
    print("O valor da passagem é R$ {:.2f}".format(distancia * 0.45))
