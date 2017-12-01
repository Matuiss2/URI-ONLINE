data = input().split()
inicial = float(data[0])
final = float(data[1])
porcentagem = ((final * 100) / inicial) - 100
print(format(porcentagem, ".2f") + "%")