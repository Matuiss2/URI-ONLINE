from math import sqrt
data = input().split()
a = float(data[0])
b = float(data[1])
c = float(data[2])
delta = (b * b) - (4 * a * c)
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (- b + sqrt(delta)) / (2 * a)
    r2 = (- b - sqrt(delta)) / (2 * a)
    print("R1 =", format(r1, ".5f"))
    print("R2 =", format(r2, ".5f"))
