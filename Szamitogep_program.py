from Szamitogep import Szamitogep


peldany1 = Szamitogep("win", 32)
peldany2 = Szamitogep("mac", 16)
peldany3 = Szamitogep("win", 16)

szamitogepek = []
szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram})")

print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(round(gyujto/len(szamitogepek), 3))

print("Legtöbb ramot tartalmazó oprendszer: ", end="")
max_index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[max_index].ram:
        max_index = i
print(szamitogepek[max_index].oprsz)



vizsgaltRam = 16
print("Van-e olyan gép aminek", vizsgaltRam,"-nál több RAM-ja van? ")
van = False
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > vizsgaltRam and szamitogepek[i].oprsz == "win":
        van = True
if van == True:
    print("van")
else:
    print("nincs")



print("Hány db windows gép van? ")
db = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        db += 1
print(db)

