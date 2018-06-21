hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
if hora_final == hora_inicial == minuto_inicial == minuto_final:
    horas, minutos = 24, 0
else:
    if minuto_final >= minuto_inicial:
        minutos = minuto_final - minuto_inicial
    else:
        minutos = 60 - abs(minuto_final - minuto_inicial)
        hora_final -= 1
    if hora_final >= hora_inicial:
        horas = hora_final - hora_inicial
    else:
        horas = 24 - abs(hora_final - hora_inicial)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
