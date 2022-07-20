n = input("Digite um número: ").strip()

if 100 < int(n) < 1000:
    n = "0"+n
elif int(n) < 100:
    n = "00"+n

print("O número digitado foi {}".format(n))
print("unidade: {}".format(n[3]))
print("dezena: {}".format(n[2]))
print("centena: {}".format(n[1]))
print("milhar: {}".format(n[0]))
