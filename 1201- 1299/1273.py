count = 0
while True:
    loops = int(input())
    if loops == 0:
        break
    names = []
    tamanhos = []
    for i in range(loops):
        data = input()
        names.append(data)  # pega todas as palavras e põe em uma lista
        tamanhos.append(len(data))  # junta o tamanho das palavras em uma lista
    if count:  # para não dar PE...
            print()
    count += 1
    for j in names:
        # pega o tamanho da maior palavra e coloca esse tamanho como margem final pras outras usando rjust
        print(j.rjust(max(tamanhos)))