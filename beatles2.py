f = open("beatles.txt", "r", encoding="utf8")
for linea in f:
    for caracter in linea:
        print(caracter, end= " ")
    print()
f.close()
    