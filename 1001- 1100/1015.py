from math import sqrt
x1y1 = input().split()
x2y2 = input().split()
x1 = float(x1y1[0])
y1 = float(x1y1[1])
x2 = float(x2y2[0])
y2 = float(x2y2[1])
print(format(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), ".4f"))
