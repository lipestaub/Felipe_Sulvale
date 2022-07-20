altura = float(input("Qual é a altura da parede? "))
largura = float(input("Qual é a largura da parede? "))

print("A parede possui {:.2f} m^2! Você precisará de {:.2f} litros de tinta para pintá-la.".format(altura*largura, altura*largura/2))