def raj_win(i, j):
    if i == "tesoura":
        if j == "papel" or j == "lagarto":
            return True
    elif i == "papel":
        if j == "pedra" or j == "spock":
            return True
    elif i == "pedra":
        if j == "tesoura" or j == "lagarto":
            return True
    elif i == "lagarto":
        if j == "spock" or j == "papel":
            return True
    else:
        if j == "tesoura" or j == "pedra":
            return True
loops = int(input())
for i in range(loops):
    data = input().split()
    raj = data[0].lower()
    shel = data[1].lower()
    if raj == shel:
        print("empate")
    elif raj_win(raj, shel):
        print("rajesh")
    else:
        print("sheldon")
