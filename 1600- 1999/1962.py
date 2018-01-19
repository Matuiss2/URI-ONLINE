for i in range(int(input())):
    data = 2015 - int(input())
    if data <= 0:
        print(abs(data - 1), "A.C.")
    else:
        print(data, "D.C.")