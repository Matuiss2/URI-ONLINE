data = input().split(" ")
x = int(data[0])
y = int(data[1])
cont = x
lista = []


def exibe_lista(l, char):
    return str(char).join([str(i) for i in l])


for j in range(1, y + 2):
    if cont == 0:
        print(exibe_lista(lista, " "))
        lista = []
        cont = x
    if cont >= 1:
        lista.append(j)
        cont -= 1