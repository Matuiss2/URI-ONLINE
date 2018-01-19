# é o mais eficiente do site em python, eu elimino a maioria dos casos nas 2 primeiras condições aumentando a eficiencia
# Mesmo assim, não é um código bom para leitura pois as vaiáveis podem confundir
for i in range(int(input())):
    """
    Recebe o input, remove o x (que entraria na lista causando um erro)converte para 
    int põe em uma lista e depois atribui os valores às variaveis"""
    time1_casa, time2_visitante = list(map(int, input().replace("x", "").split()))
    time2_casa, time1_visitante = list(map(int, input().replace("x", "").split()))
    if time1_casa > time2_visitante and time1_visitante > time2_casa:
        print("Time 1")
    elif time2_casa > time1_visitante and time2_visitante > time1_casa:
        print("Time 2")
    else:
        # essa variável reduz a necessidade de várias outras condições que deixariam o código  mais devagar
        saldo = time1_casa + time1_visitante - time2_visitante - time2_casa
        if saldo > 0:
            print("Time 1")
        elif saldo < 0:
            print("Time 2")
        elif time1_visitante > time2_visitante:
            print("Time 1")
        elif time2_visitante > time1_visitante:
            print("Time 2")
        else:
            print("Penaltis")