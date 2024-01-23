from Szamitogep import Szamitogep
def lista_letrehozas():
    peldany1 = Szamitogep("win", 32)
    peldany2 = Szamitogep("mac", 16)
    peldany3 = Szamitogep("win", 16)

    szamitogepek = []
    szamitogepek.append(peldany1)
    szamitogepek.append(peldany2)
    szamitogepek.append(peldany3)
    return szamitogepek

def lista_kiiras(szamitogepek):
    for i in range(len(szamitogepek)):
        oprsz = szamitogepek[i].oprsz
        ram = szamitogepek[i].ram
        print(f"{oprsz} ({ram})")

# lista_kiiras(lista_letrehozas())

def osszegzes_tetel(szamitogepek):
    print("Átlag: ")
    gyujto = 0
    for i in range(len(szamitogepek)):
        gyujto += szamitogepek[i].ram
    print(round(gyujto / len(szamitogepek), 3))


# osszegzes_tetel(lista_letrehozas())

def maximus_kivalasztas(szamitogepek):
    print("Legtöbb ramot tartalmazó oprendszer: ")
    max_index = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > szamitogepek[max_index].ram:
            max_index = i
    print(szamitogepek[max_index].oprsz)

# maximus_kivalasztas(lista_letrehozas())

def eldontes_tetel(szamitogepek):
    vizsgaltRam = 16
    print("Van-e olyan gép aminek", vizsgaltRam, "-nál több RAM-ja van? ")
    van = False
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > vizsgaltRam and szamitogepek[i].oprsz == "win":
            van = True
    if van == True:
        print("van")
    else:
        print("nincs")

# eldontes_tetel(lista_letrehozas())

def megszamlalas_tetel(szamitogepek):
    print("Hány db windows gép van? ")
    db = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].oprsz == "win":
            db += 1
    print(db)

# megszamlalas_tetel(lista_letrehozas())