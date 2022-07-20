from datetime import date

maioresIdade = 0
menoresIdade = 0
anoAtual = date.today().year

for i in range(1, 8):
    anoNascimento = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i)))

    if (anoAtual - anoNascimento) >= 18:
        maioresIdade = maioresIdade + 1
    else:
        menoresIdade = menoresIdade + 1

print("Dentre essas 7 pessoas, {} são maiores de idade e {} são menores de idade.".format(maioresIdade, menoresIdade))
