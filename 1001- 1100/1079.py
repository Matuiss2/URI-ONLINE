loops = int(input())
for i in range(loops):
    data = input().split()
    print(format(((float(data[0]) * 2) + (float(data[1]) * 3) + (float(data[2]) * 5)) / 10, ".1f"))
# split(), separa os valores em itens de uma lista, eu só converti cada valor para float e fiz a conta do enunciado
