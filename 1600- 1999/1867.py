while True:
    n1, n2 = input().split()
    if int(n1) + int(n2) == 0:
        break
    while True:
        total_1 = 0
        total_2 = 0
        for i in n1:
            total_1 += int(i)  # soma todos os digitos
            n1 = str(total_1)
            # converte para string para poder iterar da mesma maneira novamente(caso não tenha apenas 1 digito)
        for j in n2:
            total_2 += int(j)
            n2 = str(total_2)
        if len(n1) == 1 and len(n2) == 1:  # só vai parar de iterar qnd tiver apenas 1 digito em cada 1 dos inputs
            break
    if int(total_1) > int(total_2):
        print(1)
    elif int(total_2) > int(total_1):
        print(2)
    else:
        print(0)