import math
for i in range(int(input())):
    data = int(input())
    print("{} kg".format(math.floor(math.pow(2, data)/12000)))