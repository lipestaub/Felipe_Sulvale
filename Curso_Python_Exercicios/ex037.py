numeroInteiro = int(input("Digite o número que será convertido: "))

codigoConversao = int(input("- 1 para binário\n- 2 para octal\n- 3 para hexadecimal\nDigite o código da base de "
                            "conversão de acordo com a tabela: "))

if codigoConversao == 1 or codigoConversao == 2 or codigoConversao == 3:
    if codigoConversao == 1:
        print("O número inteiro {} é equivalente a {} em binário.".format(numeroInteiro, bin(numeroInteiro)[2:]))
    elif codigoConversao == 2:
        print("O número inteiro {} é equivalente a {} em binário.".format(numeroInteiro, oct(numeroInteiro)[2:]))
    elif codigoConversao == 3:
        print("O número inteiro {} é equivalente a {} em binário.".format(numeroInteiro, hex(numeroInteiro).upper()[2:]))
else:
    print("Opção inválida!")
