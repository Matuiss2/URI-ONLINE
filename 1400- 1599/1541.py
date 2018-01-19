import math
while True:
    '''tive q por tudo em uma variável por causa da condição de fechamento
     se eu dividisse em 3 variáveis antes iria dar erro no último input'''
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    a = data[0]
    b = data[1]
    c = data[2]
    print(math.floor(math.sqrt((a * b * 100) / c)))