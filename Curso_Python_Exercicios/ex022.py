nome = input("Digite seu nome completo: ").strip()

print("Seu nome em letras maiúsculas: " + nome.upper())
print("Seu nome em letras minúsculas: " + nome.lower())
print("Seu nome possui {} letras!".format(len(nome.replace(" ", ""))))
print("Seu primeiro nome é: {}".format(nome.split()[0]))
print("Seu primeiro nome possui {} letras!".format(len(nome.split()[0])))