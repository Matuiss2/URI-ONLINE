def main():
    n = int(input())
    for x in range(0, n):
        line = str(input(""))
        split = line.split(" ")
        n1 = int(split[0])
        d1 = int(split[2])
        op = split[3]
        n2 = int(split[4])
        d2 = int(split[6])

        if op == '+':
            n3 = (n1*d2 + n2*d1)
            d3 = (d1*d2)
            mdc = int(euclides(max(n3, d3), min(n3, d3)))
            print(str(n3) + "/" + str(d3) + " = " + str(int(n3/mdc)) + "/" + str(int(d3/mdc)))
        elif op == '-':
            n3 = (n1*d2 - n2*d1)
            d3 = (d1*d2)
            mdc = abs(int(euclides(max(n3, d3), min(n3, d3))))
            print(str(n3) + "/" + str(d3) + " = " + str(int(n3/mdc)) + "/" + str(int(d3/mdc)))
        elif op == '*':
            n3 = (n1*n2)
            d3 = (d1*d2)
            mdc = int(euclides(max(n3, d3), min(n3, d3)))
            print(str(n3) + "/" + str(d3) + " = " + str(int(n3/mdc)) + "/" + str(int(d3/mdc)))
        elif op == '/':
            n3 = (n1*d2)
            d3 = (n2*d1)
            mdc = int(euclides(max(n3, d3), min(n3, d3)))
            print(str(n3) + "/" + str(d3) + " = " + str(int(n3/mdc)) + "/" + str(int(d3/mdc)))


def euclides(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return euclides(y, r)


if __name__ == "__main__":
    main()
