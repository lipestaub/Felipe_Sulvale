n = int(input("Digite um número: ").strip())

print("O número digitado foi {}".format(n))
print("unidade: {}".format(n//1%10))
print("dezena: {}".format(n//10%10))
print("centena: {}".format(n//100%10))
print("milhar: {}".format(n//100%10))
