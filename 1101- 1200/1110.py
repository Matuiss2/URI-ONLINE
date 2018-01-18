# deve ter uma formula matematica para deixar isso bem + rápido e também seria + rapido usar deque em vez de listas
while True:
    qnt = int(input())
    if qnt == 0:
        break
    inicial = []
    for i in range(1, qnt + 1):
        inicial.append(i)
    descartado = []
    while len(inicial) > 1:
        # descarta o 1° item da lista inicial e põe na pilha de descartados
        descartado.append(inicial.pop(0))
        # faz o mesmo q a linha acima e modifica a lista inicial de acordo com o enunciado
        inicial.insert(len(inicial)-1, inicial.pop(0))
    print("Discarded cards:", ", ".join(map(str, descartado)))
    print("Remaining card:", str(inicial[0]))