nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print("Parabéns! Você está aprovado, sua média foi {:.2f}.".format(media))
elif 5 <= media <= 6.9:
    print("Você está em recuperação! Sua média foi {:.2f}.".format(media))
else:
    print("Você está reprovado! Sua média foi {:.2f}.".format(media))
