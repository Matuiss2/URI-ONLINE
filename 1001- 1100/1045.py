data = input().split()
ordenado_data = sorted(map(float, data))  # tranforma os itens em float e ordena
lado1 = ordenado_data[2]
lado2 = ordenado_data[1]
lado3 = ordenado_data[0]
if lado1 >= lado2 + lado3:
    print("NAO FORMA TRIANGULO")
else:
    if lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
        print("TRIANGULO RETANGULO")
    elif lado1 * lado1 > lado2 * lado2 + lado3 * lado3:
        print("TRIANGULO OBTUSANGULO")
    elif lado1 * lado1 < lado2 * lado2 + lado3 * lado3:
        print("TRIANGULO ACUTANGULO")
    if lado1 == lado2 == lado3:
        print("TRIANGULO EQUILATERO")
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("TRIANGULO ISOSCELES")
