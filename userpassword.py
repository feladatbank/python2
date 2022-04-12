'''
Bejelentkezés

Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! 
A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. 
A program egyetlen felhasználó (sis) jelszavát (1234) ismeri, csak ezt a párost fogadja el helyesként. 
Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adja meg a felhasználónevét! sis
Adja meg a jelszavát! 1234
Belépés engedélyezve.
-----
Adja meg a felhasználónevét! Bagaméri
Adja meg a jelszavát! A kankalin sötétben virágzik!
Belépés megtagadva.
Adja meg a felhasználónevét! bori69
Adja meg a jelszavát! hibásjelszó
Belépés megtagadva.
Adja meg a felhasználónevét! hibásfelhasználó
Adja meg a jelszavát! Jelszooo
Belépés megtagadva.
Adja meg a felhasználónevét! sis
Adja meg a jelszavát! 1234
Belépés engedélyezve.
'''

user = input("Kérem a felhasználó nevét!")
password = input("Kérem a jelszót!")


felhasznalo_nev = "sis"
jelszo = "1234"

while True:
    felhaszn = input('Kérem a felhasználónevét: ')
    jelsz = input('Kérem a jelszót: ')
    if felhaszn == felhasznalonev and jelsz == jelszo:
        print('Belépés engedélyezve!')
        break
    elif felhaszn or jelsz != felhasznalonev and jelszo:
        print('Belépés megtagadva!')
