for i in range(int(input())):
    numero = int(input())
    if numero == 0:
        print("NULL")
    else:
        if numero % 2:
            print("ODD", end=" ")
        else:
            print("EVEN", end=" ")
        if numero > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
