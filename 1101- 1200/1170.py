loops = int(input())
for i in range(loops):
    data = float(input())
    dias = 0
    while data > 1:
        data /= 2
        dias += 1
    print(dias, "dias") 
