# É só procurar pela fórmula para area de base e altura de cilindros
while True:
    try:
        volume = float(input())
        raio = float(input()) / 2
    except EOFError:
        break
    area_base = 3.14 * raio * raio
    print("ALTURA = {}".format(format(volume / area_base, ".2f")))
    print("AREA = {}".format(format(area_base, ".2f")))