"""
Feladat:
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás
segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
"""

#megtoldás:

lista= []
for i in range(3):
    nev = input("Kérek egy szót: ")
    lista.append(nev)
def legrovidebb():
    kicsi = lista[0]
    for i in lista:
        if len(i) > len(kicsi):
            i = kicsi
    return print(f"A legrövidebb szó: {i}")
legrovidebb()
