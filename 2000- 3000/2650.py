data = input().split()
for i in range(int(data[0])):
    titan = input().split()
    name = titan[:-1]  # só pega o nome do titan
    size = int(titan[-1])  # pega o tamanho e tranforma em int
    final = ""
    if size > int(data[1]):
        for j in name:
            final += j + " "  # retorna o nome do titan separando por espaços
        print(final[:-1])  # retira o último espaço