nome = input("Digite seu nome completo: ").strip()

array = nome.split()

input("Primeiro nome: {}\nÚltimo nome: {}".format(array[0], array[len(array)-1]))
