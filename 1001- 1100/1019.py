segundos_total = int(input())
horas = segundos_total // 3600
minutos = (segundos_total - (horas * 3600)) // 60
segundos = (segundos_total - (horas * 3600)) - (minutos * 60)
print("{}:{}:{}".format(horas, minutos, segundos))
