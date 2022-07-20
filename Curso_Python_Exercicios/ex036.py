valorCasa = float(input("Qual é o valor da casa? R$ "))
salario = float(input("Qual é o seu salário? R$ "))
tempo = int(input("Em quantos você quitará sua dívida? "))

prestacaoMensal = valorCasa/(tempo*12)

if prestacaoMensal > (salario*0.3):
    print("Empréstimo negado! A prestação mensal custaria R$ {:.2f}.".format(prestacaoMensal))
else:
    print("Empréstimo aprovado! Você pagará R$ {:.2f} por mês durante {} meses.".format(prestacaoMensal, tempo*12))
