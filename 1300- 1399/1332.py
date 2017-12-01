def checando_numero(palavra):
    if len(palavra) == 5:  # 1 e 2 tem 3 de tamanho em inglês
        print(3)
    else:
        val = 0
        o = 'one'
        for x in range(len(palavra)):
            if palavra[x] == o[x]:  # valores equivalentes a one
                val += 1
        if val == 2 or val == 3: # se tiver dois ou 3 equivalentes é 1
            print(1)
        else:
            print(2)


loops = int(input())  # Vê a qntd de casos testes
for i in range(loops):
    data = input()
    checando_numero(data)