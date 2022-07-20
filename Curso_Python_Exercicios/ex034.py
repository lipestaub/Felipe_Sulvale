salario = float(input("Qual é o seu salário? R$ "))

if salario<=1250:
    aumento = salario*0.15
    nSalario = salario+aumento

    print("Você receberá um aumento de R$ {:.2f} e passará a receber R$ {:.2f} por mês.".format(aumento, nSalario))
else:
    aumento = salario * 0.10
    nSalario = salario + aumento

    print("Você receberá um aumento de R$ {:.2f} e passará a receber R$ {:.2f} por mês.".format(aumento, nSalario))