dias = int(input("O carro foi alugado por quantos dias? "))
km = float(input("O carro rodou quantos km? "))

print("O valor total a pagar é R$ {:.2f}, R$ {:.2f} em diária(s) + R$ {:.2f} pela distância percorrida.".format((dias*60)+(km*0.15), dias*60, km*0.15))