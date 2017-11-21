import math
loops = int(input())
for i in range(loops):
    data = input().split()
    quantidade = int(data[0])  # Pega a quantidade de valores, é nescessário para ver o número do meio
    metade = math.ceil(quantidade / 2)  # math.ceil ja retorna o valor arredondado pra cima em int
    print("Case " + str(i + 1) + ":", data[metade])  # Seu IDE vai dar warning , ignore, math.ceil smp retorna val int