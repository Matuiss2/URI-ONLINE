loops = int(input())
for i in range(loops):
    data = input().split()
    inicial = int(data[0])
    seq = int(data[1])
    valor_ini = inicial
    for j in range(inicial, inicial + (seq * 2)):
        if j % 2 != 0:
            valor_ini += j
    print(valor_ini - inicial)