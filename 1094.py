loops = int(input())
total = 0  # total inicial de cobaias
total_c = 0  # total inicial de coelhos
total_r = 0  # total inicial de ratos
total_s = 0  # total inicial de sapos
for i in range(loops):
    data = input().split()
    qnt, tipo = int(data[0]), data[1]
    total += qnt
    if tipo == "C":
        total_c += qnt
    elif tipo == "R":
        total_r += qnt
    else:
        total_s += qnt
print("Total:", total, "cobaias")
print("Total de coelhos:", total_c)
print("Total de ratos:", total_r)
print("Total de sapos:", total_s)
print("Percentual de coelhos:", format(total_c / total * 100, ".2f"), "%")
print("Percentual de ratos:", format(total_r / total * 100, ".2f"), "%")
print("Percentual de sapos:", format(total_s / total * 100, ".2f"), "%")