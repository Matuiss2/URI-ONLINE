caso = 0
while True:
    try:
        data = int(input())
    except EOFError:
        break
    caso += 1
    lista_numero = ["0"]  # O meu método excluí o 0, então eu tive que por ele direto na lista inicial
    if data == 0:
        print("Caso {}: 1 numero\n0".format(caso))
    else:
        for i in range(data + 1):
            for j in range(i):  # põe todos os números na lista, eles se repetem de acordo com seu valor numérico
                lista_numero.append(str(i))
                # Converti para str para poder usar o método .join(que é bem superior em desempenho a usar loops)
        print("Caso {}: {} numeros\n{}".format(caso, len(lista_numero), " ".join(lista_numero)))
    print()