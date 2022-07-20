temperatura = float(input("Digite a temperatura em °C: "))

print("{:.1f}°C corresponde a {:.1f}°F e {:.1f}°K".format(temperatura, (temperatura*1.8)+32, temperatura+273.15))