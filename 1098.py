i = 0
j = 0
for k in range(11):
    for l in range(1, 4):
        print("I=" + str(format(i, ".1f")).replace(".0", ""), "J=" + str(format(l + j, ".1f").replace(".0", "")))
    # Tive que colocar o replace para retirar o .0 dos números para não dar presentation error
    j += 0.2
    i += 0.2




