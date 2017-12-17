data = input().split()
otavio = float(data[0])
bruno = float(data[1])
ian = float(data[2])

if otavio < min(ian, bruno):
    print("Otavio")
elif bruno < min(ian, otavio):
    print("Bruno")
elif ian < min(otavio, bruno):
    print("Ian")
else:
    print("Empate")