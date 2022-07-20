from math import sin, cos, tan, radians

angulo = int(input("Digite o valor do ângulo: "))

print("Os valores do seno, cosseno e tangente de {}° são, respectivamente:\n{:.2f}\n{:.2f}\n{:.2f}".format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))