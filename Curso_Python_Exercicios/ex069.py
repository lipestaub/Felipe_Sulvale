from time import sleep

pessoasComMaisDe18Anos = 0
totalHomens = 0
mulheresComMenosDe20Anos = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (F/M): ").upper().strip()
    while sexo != "M" and sexo != "F":
        print("Sexo inválido!")
        sexo = input("Digite o sexo (F/M): ").upper().strip()
    if sexo == "F":
        if idade < 20:
            mulheresComMenosDe20Anos += 1
    else:
        totalHomens += 1
    if idade > 18:
        pessoasComMaisDe18Anos += 1
    continuar = input("Deseja continuar? (S/N): ").upper().strip()
    while continuar != "S" and continuar != "N":
        print("Entrada inválida!")
        continuar = input("Deseja continuar? (S/N): ").upper().strip()
    if continuar == "N":
        break
sleep(1)
print(f"Foram cadastrados(as):\n{pessoasComMaisDe18Anos} pessoas com mais de 18 anos!\n{totalHomens} homens!\n"
      f"{mulheresComMenosDe20Anos} mulher(es) com menos de 20 anos!")
