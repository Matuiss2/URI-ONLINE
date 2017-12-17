# Coloquei todos as combinações possíveis para duas notas em uma lista
troco = [200, 150, 120, 110, 105, 102, 100, 70, 60, 55, 52, 40, 30, 25, 22, 20, 15, 12, 10, 7,  4]
while True:
    data = input().split()
    if int(data[0]) + int(data[1]) == 0:
        break
    if int(data[1]) - int(data[0]) in troco:
        print("possible")
    else:
        print("impossible")