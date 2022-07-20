valorProduto = float(input("Digite o valor do produto: R$ "))
codigoFormaPagamento = int(input("- 1 -> à vista (dinheiro/cheque)\n- 2 -> à vista (cartão)\n"
                           "- 3 -> atá 2x no cartão\n- 4 -> 3x ou mais no cartão\nDigite o código da forma de "
                                 "pagamento de acordo com a tabela acima: "))

if codigoFormaPagamento == 1:
    precoFinal = valorProduto-(valorProduto*0.1)
    print("Preço final = R$ {:.2f}".format(precoFinal))
elif codigoFormaPagamento == 2:
    precoFinal = valorProduto-(valorProduto*0.05)
    print("Preço final = R$ {:.2f}".format(precoFinal))
elif codigoFormaPagamento == 3:
    precoFinal = valorProduto
    print("Preço final = R$ {:.2f}, em 2 vezes de R$ {:.2f}".format(precoFinal, precoFinal/2))
elif codigoFormaPagamento == 4:
    precoFinal = valorProduto+(valorProduto*0.2)
    numeroParcelas = int(input("Qual é o número de parcelas? "))
    print("Preço final = R$ {:.2f}, em {} vezes de R$ {:.2f}".format(precoFinal, numeroParcelas, precoFinal /
                                                                     numeroParcelas))
else:
    print("Opção inválida!")

