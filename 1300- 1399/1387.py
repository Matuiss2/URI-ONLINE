while True:
    num1, num2 = list(map(int, input().split()))
    if num1 + num2 == 0:
        break
    print(num1 + num2)