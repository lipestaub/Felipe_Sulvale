velocidade = float(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    print("Você está {} Km/h acima do limite.\nValor da multa: R$ {:.2f}".format(velocidade-80, (velocidade-80)*7))
else:
    print("OK!")
