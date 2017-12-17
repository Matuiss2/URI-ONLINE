data = int(input())
if data == 1:
    print("Top 1")
elif data in range(2, 4):
    print("Top 3")
elif data in range(4, 6):
    print("Top 5")
elif data in range(6, 11):
    print("Top 10")
elif data in range(11, 26):
    print("Top 25")
elif data in range(26, 51):
    print("Top 50")
elif data in range(51, 101):
    print("Top 100")