projeto = 0
while True:
    try:
        inicial, final = map(float, input().split())
    except EOFError:
        break
    projeto += 1
    total = (final - inicial) / inicial * 100
    print("Projeto {}:".format(projeto))
    print("Percentual dos juros da aplicacao:", format(total, ".2f"), "%\n")