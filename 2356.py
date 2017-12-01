while True:
    try:
        seq1 = input()
        seq2 = input()
    except EOFError:
        break
    if seq2 in seq1:  # Se a sequencia 2 estiver contida na sequencia 1, ela é resistente
        print("Resistente")
    else:
        print("Nao resistente")
