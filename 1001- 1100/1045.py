lado3, lado2, lado1 = sorted(map(float, input().split()))
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
