data = input().split()
if max(map(int, data)) % min(map(int, data)) == 0:  # tranforma em int pega o maior e vê se é divisível pelo menor
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")