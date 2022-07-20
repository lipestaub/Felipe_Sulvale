import datetime

data = str(datetime.date.today())
anoAtual = int(data.split('-')[0])

anoNascimento = int(input("Em que você nasceu? "))

idade = anoAtual-anoNascimento

if idade <= 9:
    print("Você tem {} anos e está na categoria MIRIM!".format(idade))
elif 9 < idade <= 14:
    print("Você tem {} anos e está na categoria INFANTIL!".format(idade))
elif 14 < idade <= 19:
    print("Você tem {} anos e está na categoria JUNIOR!".format(idade))
elif 19 < idade <= 20:
    print("Você tem {} anos e está na categoria SÊNIOR!".format(idade))
else:
    print("Você tem {} anos e está na categoria MASTER!".format(idade))
