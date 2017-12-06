for i in range(10):
    data = int(input())
    if data <= 0:
        print("X[{}] = 1".format(i))
    else:
        print("X[{}] = {}".format(i, data))
