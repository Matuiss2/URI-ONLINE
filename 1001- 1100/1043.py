data = input().split()
ordenado_data = sorted(map(float, data))  # converte os itens do input para float e ordena, fica mais legível o código
lado1 = ordenado_data[2]  # O maior lado fica aqui
lado2 = ordenado_data[1]
lado3 = ordenado_data[0]  # O menor aqui
if lado1 >= lado2 + lado3:  # Eu ordenei para ficar mais consiso aqui
    print("Area =", format((float(data[0]) + float(data[1])) * float(data[2]) / 2, ".1f"))
else:
    print("Perimetro =", format((lado1 + lado2 + lado3), ".1f"))
