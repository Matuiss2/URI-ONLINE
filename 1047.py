# Esse codigo provabelment pode ser reduzido, tem muito codigo repetido
data = input().split()
if int(data[2]) <= int(data[0]):
    horas = int(data[2]) - int(data[0]) + 24   # Se for em outro dia adiciona 24h(um dia) a conta
    if int(data[3]) < int(data[1]):
        horas -= 1  # Se for em outra hora remove 1 hora da conta
else:
    horas = int(data[2]) - int(data[0])
    if int(data[3]) < int(data[1]):
        horas -= 1
if int(data[3]) < int(data[1]):
    minutos = int(data[3]) - int(data[1]) + 60  # Se for em outra hora adiciona 60 m(1h) a conta
else:
    minutos = int(data[3]) - int(data[1])

if horas == 24 and minutos:  # corrige uma falha logica do codigo, que permitia coisas como 24:12(qnd o max é 1 dia)
    horas -= 24
print("O JOGO DUROU", horas, "HORA(S) E", minutos, "MINUTO(S)")