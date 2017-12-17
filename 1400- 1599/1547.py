loops = int(input())
for i in range(loops):
    data1 = input().split()
    data2 = input().split()
    dif = []
    for j in data2:
        dif.append(abs(int(j) - int(data1[1])))  # pega a diferença de todos os valores qnd comparados ao valor certo
    print(dif.index(min(dif)) + 1)  # Retorna a posição do valor mais próximo ao correto(+ 1 pois o index começa no 0)