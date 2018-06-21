quantia = float(input()) * 1000
notas = [100000, 50000, 20000, 10000, 5000, 2000]
moedas = [1000, 500, 250, 100, 50, 10]
print("NOTAS:")
for i in notas:
    print("{} nota(s) de R$ {}".format(int((quantia) // i), format(i / 1000, ".2f")))
    quantia %= i
print("MOEDAS:")
for j in moedas:
    print("{} moeda(s) de R$ {}".format(int(quantia // j), format(j / 1000, ".2f")))
    quantia %= j
