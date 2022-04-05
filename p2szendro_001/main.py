"""
1.feladat: nyissa meg a fájlt és mentse el egy listában
"""

with open("szoveg.txt") as f:
    for i in f:
        lista = i.split(";")

"""
1.1 feladat:
Irja ki a program hogy hány darab "1" van a fájlban
"""

szamlalo = 0
for szam in lista:
    if szam == "1":
        szamlalo += 1
print(f"1.feladat: 1-esek száma a listában: {szamlalo}")

"""
1.2.feladat:
Irja ki a program hogy mennyivel van több szám a másiknál és mennyivel
"""

nulla = 0
for szam in lista:
    if szam == "0":
        nulla += 1
if szamlalo > nulla:
    print(f"2.feladat: {szamlalo - nulla}(-val vel) van több 1-es mint 0")
else:
    print(f"2.feladat: {nulla - szamlalo}(-val vel) van több 0 mint 1-es")

"""
1.3 feladat: irja ki a program hogy  hány darab szám van a fájlban
"""

print(f"3.feladat: {len(lista)} szám van a listában")

