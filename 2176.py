data = input()
if data.count("1") % 2 == 0:  # se a qnt de 1 for par adiciona um 0 no final
    print(data + "0")
else:  # se for impar  adiciona o 1 no final
    print(data + "1")