qntd = 0
total = 0
while True:
    try:
        nomes = input()
        distancia = int(input())
    except EOFError:
        break
    qntd += 1
    total += distancia
print(format(total / qntd, ".1f"))