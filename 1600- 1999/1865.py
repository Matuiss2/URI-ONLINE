loops = int(input())  # Vê a qntd de casos testes
for i in range(loops):
    data = input().split()  # Separa o nome de quem está levantando e a força utilizada
    nome = data[0]  # A força não importa só o nome
    if nome == "Thor":  # Apenas se for o thor vai levantar
        print("Y")
    else:
        print("N")
