# Smp q tiver 1 exercício q diz q o último valor é fim de arquivo ou valor EOF use esse método
while True:
    try:
        loops = int(input())  # Vê a qntd de casos testes
    except EOFError:
        break
    lista = []  # Junta todos os números aqui como strings(não converter para int, senão os 0 iniciais iriam sumir)
    for i in range(loops):
        data = input()
        lista.append(data)
    lista_ordenada = sorted(lista)  # Ordena a lista
    for j in lista_ordenada:
        print(j)  # Imprime na ordem crescente