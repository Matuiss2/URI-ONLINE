while True:
    x, y = map(int, input().split())
    if any(nulo == 0 for nulo in [x, y]):
        break
    elif all(positivo > 0 for positivo in [x, y]):
        print("primeiro")
    elif all(negativo < 0 for negativo in [x, y]):
        print("terceiro")
    elif x > 0:
        print("quarto")
    else:
        print("segundo")
