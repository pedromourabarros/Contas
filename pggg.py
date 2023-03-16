import math
print("Digite o valor de a")
a = int(input())
print("Digite o valor de b")
b = int(input())
print("Digite o valor de c")
c = int(input())
delta = math.pow(b, 2) - 4 * a * c
print("O resultado do Delta é ", delta)
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print("O resultdo da equeção é", x1,"e", x2)