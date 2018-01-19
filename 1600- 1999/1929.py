def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


A, B, C, D = list(map(int, input().split()))
if is_triangle(A, B, C):
    print("S")
elif is_triangle(A, B, D):
    print("S")
elif is_triangle(A, C, D):
    print("S")
elif is_triangle(B, C, D):
    print("S")
else:
    print("N")