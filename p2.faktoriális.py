'''irjon egy fuggvenyt ami visszatér az adott szám faktorialis osszegevel! pl: 7! = 1*2*3*4*5*6*7 = 5040'''

def faktor(szam):
    faktorialis = 1
    if szam < 0:
        return "negatív számokkal nem működik a faktor"
    elif szam == 0:
        return "0 fakt. összege 1"
    else:
        for i in range(1,szam + 1):
            faktorialis = faktorialis*i
        return f"{szam}-nak/nek a faktor. összege: {faktorialis}"

print(faktor(7))
