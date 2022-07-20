from random import choice

n1 = input("Digite o nome do(a) primeiro(a) aluno(a): ")
n2 = input("Digite o nome do(a) segundo(a) aluno(a): ")
n3 = input("Digite o nome do(a) terceiro(a) aluno(a): ")
n4 = input("Digite o nome do(a) quarto(a) aluno(a): ")

print("O aluno(a) sorteado(a) foi o(a): {}".format((choice([n1, n2, n3, n4]))))
