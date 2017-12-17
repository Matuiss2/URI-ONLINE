while True:
    data = int(input())
    if data == 0:
        break
    final = []
    for i in range(1, (data + 1)):
        borda = []
        count = i
        for j in range(data):
            borda.append(abs(count))
            if count == 1:
                count -= 3
            else:
                count -= 1
        final.append(borda)
    for k in range(data):
        tx = ''
        for j in range(data):
            # essa linha da muito trabalho quanto a PE no site(n use format() nesse caso)
            tx += " %3d" % final[k][j]
        print(tx[1:])
    print()