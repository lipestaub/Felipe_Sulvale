from random import shuffle

n1 = input("Digite o nome do(a) primeiro(a) aluno(a): ")
n2 = input("Digite o nome do(a) segundo(a) aluno(a): ")
n3 = input("Digite o nome do(a) terceiro(a) aluno(a): ")
n4 = input("Digite o nome do(a) quarto(a) aluno(a): ")

ordem = [n1, n2, n3, n4]

shuffle(ordem)

print("Ordem de apresentação: \n", ordem)