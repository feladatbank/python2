#1.1 és 1.2 feladat (összetett feladat)

#1.1 feladat
'''
1.1 feladat: open használatával készíts egy szöveges fájlt, majd írja bele a 1.2-es feladatot. A legvégén nyissa meg újra a szöveges fájlt viszont ezúttal olvasó nézetben.: 'Készíts egy olyan függvényt, amely számokat kér be, a kilépő érték egy negatív szám legyen, majd egy listában tárolja el a számokat! A függvény a lista összegét számolja ki, tartalmazza a függvény meghívását is!'
'''

#megoldás

f = open("szoveg.txt", "w")
f.write('Készíts egy olyan függvényt, amely számokat kér be, a kilépő érték egy negatív szám legyen, majd egy listában tárolja el a számokat! A függvény a lista összegét számolja ki, tartalmazza a függvény meghívását is!')
f.close()

f = open("szoveg.txt", "r")

#1.2 feladat
'''
Az előző feladatban megadott szöveg alapján készítsd el a 'main.py' fájl-ban a feladatot.
'''
#megoldás:

lista = []
while True:
    beker = int(input('Szám: '))
    lista.append(beker)
    if beker < 0:
        lista.remove(-1)
        break

        
def osszead(lista):
	eredmeny = sum(lista)
	print('A lista összege: ', eredmeny)
osszead(lista)

