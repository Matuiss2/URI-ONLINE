loops = int(input())
maior = 0
aprovados = {}
for i in range(loops):
    data = input().split()
    if float(data[1]) >= 8:  # coloca os aprovados e suas notas em um dicionário
        aprovados[data[0]] = float(data[1])

if len(aprovados) > 0:
    print(max(aprovados, key=aprovados.get))   # Pega a maior nota dos aprovados e imprime o dono dessa nota
else:  # Se n tiver aprovados entra aqui
    print("Minimum note not reached")