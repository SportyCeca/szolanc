szo = str(input("Adjon meg egy szót az angol ABC betűivel(kisbtű, 6 betű):"))
while len(szo) != 6:
    print("Kritériumnak nem felel meg!")
    szo = str(input("Adjon meg egy szót az angol ABC betűivel(kisbtű, 6 betű):"))

for b in szo:
    if ord(b) < 97 or ord(b) > 122:
        print("Nem megfelelő karaktereket használ!")