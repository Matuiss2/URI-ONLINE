numeros = list(map(int, input().split()))
if max(numeros) % min(numeros):
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")
