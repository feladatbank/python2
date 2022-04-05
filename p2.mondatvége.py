'''
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhajtó)
########################################################################################################################################################################
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program (amig a felhasználó csak egy ENTER-t nem üt), majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!
'''

while True:
        
    beker = input('mondat: ')
    if beker == '':
        break
    elif beker[-1] == '?':
        print('kérdőmondat')

    elif beker[-1] == '.':
        print('kijelentő mondat')

    elif beker[-1] == '!' and 'Bárcsak' in beker or 'bárcsak' in beker:
        print('óhajtó')

    elif beker[-1] == '!' and 'Bárcsak' not in beker or 'bárcsak'  not in  beker :
        print('Felkialto mondat')
