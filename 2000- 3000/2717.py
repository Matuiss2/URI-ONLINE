final = int(input())
preciso = sum(list(map(int, input().split())))
if preciso > final:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")