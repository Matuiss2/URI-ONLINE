inicial, segundo, lista_fibonacci, loops = 0, 1, ["0", "1"], int(input())
if loops == 1:
    print("0")
elif loops == 2:
    print("0 1")
else:
    for i in range(loops - 2):
        lista_fibonacci.append(inicial + segundo)
        inicial, segundo = segundo, inicial + segundo
    print(" ".join(map(str, lista_fibonacci)))
