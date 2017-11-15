data = input().split()
A = float(data[0])
B = float(data[1])
C = float(data[2])
pi = 3.14159
tri = (A * C) / 2
cir = (pi * C * C)
tra = (C * (A + B)) / 2
ret = A * B
qua = B * B
print("TRIANGULO:", format(tri, ".3f"))
print("CIRCULO:", format(cir, ".3f"))
print("TRAPEZIO:", format(tra, ".3f"))
print("QUADRADO:", format(qua, ".3f"))
print("RETANGULO:", format(ret, ".3f"))