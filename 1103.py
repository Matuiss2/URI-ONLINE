while True:
    data = input().split()
    h1 = int(data[0])
    m1 = int(data[1])
    h2 = int(data[2])
    m2 = int(data[3])
    if h1 + h2 + m1 + m2 == 0:
        break
    minutos_atuais = (h1 * 60) + m1  # Total de minutos no dia quando ela foi dormir
    minutos_finais = (h2 * 60) + m2  # Total de minutos no dia quando ela for acordar
    if minutos_atuais < minutos_finais:  # Se o dia for o mesmo(que ela dormir e acordar) entra aqui
        print(abs(minutos_atuais - minutos_finais))  # abs para converter pra positivo(o resultado sempre será negativo)
    else:
        # Se o dia for outro vai se substrair 1440 minutos(representando 1 dia) assim mostrando o valor certo
        print(abs(minutos_atuais - minutos_finais - 1440))