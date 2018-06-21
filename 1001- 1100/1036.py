a, b, c = map(float, input().split())
delta = (b * b) - (4 * a * c)
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (- b + delta ** 0.5) / (2 * a)
    r2 = (- b - delta ** 0.5) / (2 * a)
    print("R1 = {}\nR2 = {}".format(format(r1, ".5f"), format(r2, ".5f")))
