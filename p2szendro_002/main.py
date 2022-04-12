#1.feladat:
#irja ki a program hogy hány szóból áll a lista:
lista= []
with open("szavak.txt", "r") as f:
    for i in f:
        lista.append(i.strip())
print(f"1. feladat:{len(lista)} szóbol áll a lista.")
        

#2.feladat:
#Irj egy programot ami kiválaszt egy véletlen szót a listábol és ki is irja a képernyőre.
import random

with open("szavak.txt", "r") as f:
    sor = f.readlines()

szo = random.choice(sor).strip()
print(f"2. feladat:A véletlenül kiválasztott szó: {szo}")

#3.feladat:
#Irja ki a program hogy hány betűből áll a véletlenül kiválasztott szó.

print(f"3. feladat:A {szo} {len(szo)} betű-ből áll")

#4.feldat:
#Irja ki a program a leghosszab szót
legnagyobb = lista[0]
for i in lista:
    if len(legnagyobb) > len(i):
        legnagyobb = legnagyobb
    else:
        legnagyobb = i
print(f"4. feladat:A leghosszabb szó: {legnagyobb}")