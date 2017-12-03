# Com toda a certeza tem maneiras mais eficientes de fazer esse código
osso = input()[0]  # coloquei o index em todos os inputs pra não precisar digitar tudo
if osso == "v":
    classe = input()[0]
    if classe == "a":
        comida = input()[0]
        if comida == "c":
            print("aguia")
        else:
            print("pomba")
    else:
        comida = input()[0]
        if comida == "o":
            print("homem")
        else:
            print("vaca")
else:
    classe = input()[0]
    if classe == "i":
        comida = input()[2]
        if comida == "m":
            print("pulga")
        else:
            print("lagarta")
    else:
        comida = input()[0]
        if comida == "h":
            print("sanguessuga")
        else:
            print("minhoca")
