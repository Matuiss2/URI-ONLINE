# Esse exercício era mais interpretação de texto q um exercício de programação
loops = int(input())
for i in range(loops):
    data = input().split()
    horas, minutos, porta = data
    if int(horas) < 10:
        horas = "0" + str(horas)
    if int(minutos) < 10:
        minutos = "0" + str(minutos)
    if porta == "1":
        print("{}:{} - A porta abriu!".format(horas, minutos))
    else:
        print("{}:{} - A porta fechou!".format(horas, minutos))