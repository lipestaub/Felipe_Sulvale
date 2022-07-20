valorTotal = 0
qtdProdutosQueCustamMaisDe1000 = 0
nomeProdutoMaisBarato = ""
valorProdutoMaisBarato = 0
isFirst = True
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Valor: R$ "))
    if isFirst:
        nomeProdutoMaisBarato = nome
        valorProdutoMaisBarato = valor
        isFirst = False
    elif valor < valorProdutoMaisBarato:
        nomeProdutoMaisBarato = nome
        valorProdutoMaisBarato = valor
    if valor > 1000:
        qtdProdutosQueCustamMaisDe1000 += 1
    valorTotal += valor
    continuar = input("Deseja continuar? (S/N): ").upper().strip()
    while continuar != "S" and continuar != "N":
        print("Entrada inválida!")
        continuar = input("Deseja continuar? (S/N): ").upper().strip()
    if continuar == "N":
        break
print(f"O total da compra foi R$ {valorTotal:.2f}\n"
      f"{qtdProdutosQueCustamMaisDe1000} custaram mais de R$ 1000,00\n"
      f"O produto mais barato foi o(a) {nomeProdutoMaisBarato}, que custou R$ {valorProdutoMaisBarato:.2f}"
      .replace(".", ','))
