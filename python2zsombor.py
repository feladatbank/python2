# Csinálj egy függvényt / funkciót aminek meg lehet adni 5 számot, ezután vissza adja az 5 szám közül a legkissebb és a legnagyobb számot és az összegüket.


def szam(a, b, c, d, e):
    lista = [a, b, c, d, e]
    lista.sort()
    print(lista)
    print("A legkisebb szám:", lista[:1])
    print("A legnagyobb szám:", lista[4:])
    print("A számok összege: ", sum(lista))


szam(1, 2, 4, 8, 16)