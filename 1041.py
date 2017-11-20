data = input().split()
posicaox = float(data[0])
posicaoy = float(data[1])
if posicaox == 0 and posicaoy == 0:
    print("Origem")
elif posicaox == 0:
    print("Eixo Y")
elif posicaoy == 0:
    print("Eixo X")
elif posicaox > 0:
    if posicaoy > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if posicaoy > 0:
        print("Q2")
    else:
        print("Q3") 