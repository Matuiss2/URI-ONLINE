pulo = input().split()
data = input().split()
ultimo = int(pulo[0])
for i in data:
    # Se a diferenca entre um cano e outro for maior que o pulo vai dar game over
    if abs(int(i) - ultimo) > int(pulo[0]):
        print("GAME OVER")
        break
    ultimo = int(i)
else:
    print("YOU WIN")
