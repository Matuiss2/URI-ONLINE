data = float(input())
for i in range(100):
    print("N[{}] = {}".format(i, format(data, ".4f")))
    data /= 2
