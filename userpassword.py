'''
Bejelentkezés

Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! 
A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. 
A program egyetlen felhasználó (bori99) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. 
Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Szivecske<3
Belépés engedélyezve.
-----
Adja meg a felhasználónevét! Bagaméri
Adja meg a jelszavát! A kankalin sötétben virágzik!
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! hibásjelszó
Belépés megtagadva.
Adja meg a felhasználónevét! hibásfelhasználó
Adja meg a jelszavát! Jelszo
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Jelszo
Belépés engedélyezve.
'''

user = input("Kérem a felhasználó nevét!")
password = input("Kérem a jelszót!")


felhasznalo_nev = "bori99"
jelszo = "Jelszo"

while True:
  if user == felhasznalo_nev:
    print("Sikeres felhasználónév!")
    break
  if password == jelszo:
    print("Sikeres jelszó")
    break
  if user == felhasznalo_nev and password == jelszo:
    print("Most be vagy jelentkezve!" '/n' "Üdvözlünk!", felhasznalo_nev)
    break
  if user != felhasznalo_nev:
    print("Sikertelen a felhasználónév!")
    break
  if password != jelszo:
    print("Sikertelen a jelszó!")
    break
  if user != felhasznalo_nev and password != jelszo:
    print("Sikertelen a jelszava, és a felhasználónév!")
    break
