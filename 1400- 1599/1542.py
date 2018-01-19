while True:
    '''tive q por tudo em uma variável por causa da condição de fechamento
     se eu dividisse em 3 variáveis antes iria dar erro no último input'''
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    x = int((data[0] * data[1]) / (data[2] - data[0]) * data[2])
    if x == 1:
        print("{} pagina".format(x))  # print(x, "pagina") seria mais rápido
    else:
        print("{} paginas".format(x))