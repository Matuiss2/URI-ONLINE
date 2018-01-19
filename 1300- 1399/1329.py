while True:
    total = int(input())
    if total == 0:
        break
    mary = input().count("0")
    print("Mary won {} times and John won {} times".format(mary, total - mary))