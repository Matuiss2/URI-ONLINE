# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        loops = input().split()
    except EOFError:
        break
    notas = []
    for i in range(int(loops[0])):
        data = int(input())
        notas.append(data)  # põe todas as notas em uma lista
    for j in range(int(loops[1])):
        posicao = int(input())
        # põe a lista de notas em ordem decrescente e pega a pos pedida(-1 pois as listas são contadas a partir do 0)
        print(sorted(notas, reverse=True)[posicao - 1])