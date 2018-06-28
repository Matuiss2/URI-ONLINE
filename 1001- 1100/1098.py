i = 0
while i <= 2:
    for j in range(1, 4):
        print("I={} J={}".format(format(i, ".1f"), format(j + i, ".1f")).replace(".0", ""))
    i += 0.2
