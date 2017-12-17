import math
loops = int(input())
caso = 0
for i in range(loops):
    tipo = input()
    data = input().split()
    caso += 1
    if tipo == "min":
        # tranforma os valores em int, põe em uma lista e pega o menor
        print("Caso #{}:".format(caso), min(map(int, data)))
    elif tipo == "mean":
        # tranforma os val em int, põe em uma lista e pega a média arrendondando o valor para baixo
        print("Caso #{}:".format(caso), math.floor(sum(map(int, data)) // 3))  # talvez math.floor n fosse preciso aqui
    elif tipo == "max":
        # tranforma os valores em int, põe em uma lista e pega o maior
        print("Caso #{}:".format(caso), max(map(int, data)))
    else:
        # tranforma os val em int, põe em uma lista faz a fórmula do enunciado arrendondando o valor para baixo
        print("Caso #{}:".format(caso), math.floor((int(data[0]) * 0.3 + int(data[1]) * 0.59 + int(data[2]) * 0.11))) 