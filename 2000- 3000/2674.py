# Infelizmente sympy.isprime não funciona no site pois é um módulo de terceiros
def is_prime(n):
    if n in range(0, 2):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        data = input()
    except EOFError:
        break
    if is_prime(int(data)):
        for j in data:
            if j not in "2357":
                # usando esse método é melhor que chamar a função de novo(funciona pois só tem apenas 1 digito)
                print("Primo")
                break
        else:
            print("Super")
    else:
        print("Nada")