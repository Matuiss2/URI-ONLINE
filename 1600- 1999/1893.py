passado, presente = map(int, input().split())
if presente in range(0, 3):
    print("nova")
elif presente in range(3, 97):
    if passado > presente:
        print("minguante")
    else:
        print("crescente")
else:
    print("cheia")