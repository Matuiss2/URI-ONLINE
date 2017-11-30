loops = int(input()) # Vê a qntd de linhas
for i in range(1, loops + 1):
    print(i, i * i, i * i * i)  # o numero inicial  o numero inicial ^ 2 o numero inicial ^ 3
    for j in range(1):  # a proxima linha sempre sera a primeira mas com o 2° e 3° n° com 1 a mais
        print(i, i * i + 1, i * i * i + 1)
