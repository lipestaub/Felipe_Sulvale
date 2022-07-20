sexo = input("Digite seu sexo (M/F): ").strip().upper()

while 'M' != sexo != 'F':
    print("Entrada inválida!!\n" + "-"*20)
    sexo = input("Digite o sexo (M/F): ").upper()

if sexo == "M":
    print("Sexo 'masculino' registrado com sucesso!")
else:
    print("Sexo 'feminino' registrado com sucesso!")
