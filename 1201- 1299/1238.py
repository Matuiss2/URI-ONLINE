loops = int(input())
for i in range(loops):
    str_final = ""
    data = input().split()  # separas as palavras e elimina os espaços
    for j in range(min(len(data[0]), len(data[1]))):
        str_final += data[0][j] + data[1][j]  # pela diferença de tamanho ela itercala as letras das 2 palavras
    # Depois checa qual das 2 palavras é a maior é completa a palavra final com o que sobrou
    if len(data[0]) > len(data[1]):
        print(str_final + data[0][len(data[1]):len(data[0])])
    elif len(data[1]) > len(data[0]):
        print(str_final + data[1][len(data[0]):len(data[1])])
    else:  # se forem iguais já está completo e entra aqui
        print(str_final)