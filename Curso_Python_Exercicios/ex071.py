from math import floor

while True:
    valor = int(input("Qual valor você quer sacar? R$ "))
    qtdCelulasDe50 = floor(valor / 50)
    qtdCelulasDe20 = floor((valor % 50) / 20)
    qtdCelulasDe10 = floor((valor % 50 % 20) / 10)
    qtdCelulasDe1 = floor(valor % 50 % 20 % 10)

    if qtdCelulasDe50 != 0:
        print(f"Total de {qtdCelulasDe50} cédulas de R$ 50,00")
    if qtdCelulasDe20 != 0:
        print(f"Total de {qtdCelulasDe20} cédulas de R$ 20,00")
    if qtdCelulasDe10 != 0:
        print(f"Total de {qtdCelulasDe10} cédulas de R$ 10,00")
    if qtdCelulasDe1 != 0:
        print(f"Total de {qtdCelulasDe1} cédulas de R$ 1,00")
    continuar = input("Deseja realizar outro saque? (S/N): ").upper().strip()
    while continuar != "S" and continuar != "N":
        print("Entrada inválida!")
        continuar = input("Deseja realizar outro saque? (S/N): ").upper().strip()
    if continuar == "N":
        break
