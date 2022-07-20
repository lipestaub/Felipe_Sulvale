somaIdades = 0
nomeHomemMaisVelho = None
idadeHomemMaisVelho = 0
qtdMulheres = 0

for i in range(1, 5):
    print("----- {}ª PESSOA -----".format(i))

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = int(input("- 1 -> Feminino\n- 2 -> Masculino\nDigite o sexo de acordo com os valores acima: "))

    if sexo == 2:
        if nomeHomemMaisVelho is None:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
        elif idade > idadeHomemMaisVelho:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
    elif sexo == 1:
        if idade < 20:
            qtdMulheres = qtdMulheres + 1

    somaIdades += idade

print("A média das idades é igual a {:.1f} ano(s), o nome do homem mais velho é {} e {} mulher(es) do grupo possui(em) "
      "menos que 20 anos!".format(somaIdades/4, nomeHomemMaisVelho, qtdMulheres))
