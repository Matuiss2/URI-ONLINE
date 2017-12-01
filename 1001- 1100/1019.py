segundos = int(input())
resto_s = segundos % 60
minutos = segundos // 60
resto_m = minutos % 60
horas = minutos // 60
print(str(horas) + ":" + str(resto_m) + ":" + str(resto_s))
