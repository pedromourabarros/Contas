import math
a = b = c = 0
delta = x1 = x2 = 0.0
print("Digite o valor de a")
a = int(input())
print("Digite o valor de b")
b = int(input())
print("Digite o valor de c")
c = int(input())
delta = math.pow(b, 2) -4 * a * c
print("O resultado do Delta é ", delta)
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print("x1", x1)
print("x2", x2)


