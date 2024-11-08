f = open("beatles.txt", "r", encoding="utf8")
for linea in f:
    print(linea.strip())
f.close()
