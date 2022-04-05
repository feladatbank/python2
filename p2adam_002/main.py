'''
Készíts egy szöveges fájlt ami tetszőleges szöveget kiír a fájlon belül, fontos hogy több sorból álljon! Majd nyisd meg  a fájlt és olvasd ki a sorokat belőle, valamint jelenítsd meg.
'''

f = open('szoveg.txt', 'w', encoding='utf-8')
f.write(' Szia uram!\nSzép napunk van.\nHogy vagy?')
f.close()

f = open('szoveg.txt', 'r')

megjelenit = f.readline()
megjelenit1 = f.readline()
megjelenit2 = f.readline()

print(megjelenit,megjelenit1,megjelenit2)