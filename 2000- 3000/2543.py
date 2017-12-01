# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    videos = 0
    try:
        loops_id = input().split()
    except EOFError:
        break
    for i in range(int(loops_id[0])):
        data = input().split()
        if data[0] == loops_id[1] and int(data[1]) == 0:
            videos += 1
    print(videos)