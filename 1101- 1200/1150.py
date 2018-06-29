numero1, numero2, contador = int(input()), int(input()), 0
while numero2 <= numero1:
    numero2 = int(input())
total = numero1
while total < numero2:
    total += numero1 + contador
    contador += 1
if numero2 <= 0:
    print(contador)
else:
    print(contador + 1)
