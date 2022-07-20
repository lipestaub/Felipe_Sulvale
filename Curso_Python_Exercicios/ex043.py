from math import pow

altura = float(input("Qual é a sua altura (em m)? "))
peso = float(input("Qual é o seu peso (em kg)? "))

imc = peso/pow(altura, 2)

if imc < 18.5:
    print("IMC = {:.1f} -> Status: Abaixo do peso.".format(imc))
elif 18.5 <= imc <= 25:
    print("IMC = {:.1f} -> Status: Peso ideal.".format(imc))
elif 25 < imc <= 30:
    print("IMC = {:.1f} -> Status: Sobrepeso.".format(imc))
elif 30 < imc <= 40:
    print("IMC = {:.1f} -> Status: Obesidade.".format(imc))
else:
    print("IMC = {:.1f} -> Status: Obesidade mórbida.".format(imc))
