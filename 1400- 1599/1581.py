for i in range(int(input())):
    lista_ling = []
    for j in range(int(input())):
        ling = input()
        lista_ling.append(ling)
    # set remove os repetidos, se tiver mais de 1 língua sempre será inglês
    if len(set(lista_ling)) > 1:
        print("ingles")
    else:
        print(lista_ling[0])  # Se tiver só uma língua falada a resposta sempre será ela