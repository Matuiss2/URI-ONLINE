for i in range(int(input())):
    a, b = map(int,  input().replace("x", " ").split())
    for j in range(5, 11):
        if a == b:
            print("{} x {} = {}".format(a, j, a * j))
        else:
            print("{} x {} = {} && {} x {} = {}".format(a, j, a * j, b, j, b * j))