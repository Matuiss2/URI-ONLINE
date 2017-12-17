# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        loops = int(input())
    except EOFError:
        break
    valores = {}
    for i in range(loops):
        data = input().split()
        valores[data[0]] = int(data[1])  # põe os valores correspondentes para cada item no dicionário
    ordenado = sorted(valores, key=valores.get)  # põe os valores em ordem e retorna as chaves correspondentes
    final = ""
    for j in ordenado:
        final += j + " "  # separa os valores com um espaço (usar " ".join() é bem mais eficiente)
    print(final[:-1])  # retira o último espaço