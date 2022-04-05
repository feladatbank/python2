#Ausztria;1995.01.01
#Belgium;1958.01.01

class Csatlakozas():
    def __init__(self, sor):
        orszag, datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[:4])
        self.honap = int(datum[5:7])
        
with open("EUcsatlakozas.txt", "r", encoding="latin2") as f:
    lista = [Csatlakozas(sor) for sor in f]
    
#3
print(f"3.Feladat: EU tagállamainak száma: {len(lista)} db")

#4
szamlalo = 0
for sor in lista:
    if sor.ev == 2007:
        szamlalo = szamlalo + 1
print(f"4.Feladat: 2007-ben {szamlalo} ország csatlakozott.")
    
#5
for sor in lista:
    if sor.orszag == "Magyarország":
        q = sor.datum
print(f"5.Feladat: Magyarország csatlakozásának dátuma: {q}")
    
#6
for sor in lista:
    if sor.honap == 5:
        print("6.Feladat: Májusban volt csatlakozás!")
        break


#7       
u_csatlakozott = 0
for sor in lista:
    if sor.ev > u_csatlakozott:
        u_csatlakozott = sor.ev
        u_orszag = sor.orszag
print(f"7.Feladat: Legutoljára csatlakozott ország: {u_orszag}")
    

#8
print("8.Feladat: Statisztika")
stat = dict()
for sor in lista:
    stat[sor.ev] = stat.get(sor.ev, 0) + 1
for kulcs, ertek in stat.items():
    print(f"       {kulcs} - {ertek} ország")
    


    