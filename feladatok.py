def elso():
    print("Első feladat!")
    #Írjuk ki 0-tól 150-ig a páros számokat!
    i = 0
    while i < 150:
        i += 1
        if i % 2 == 0:
            print(i)

def masodik():
    print("Második feladat!")
    #Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
    i = 0
    oszthato_szamok = 0
    while i < 10:
        i += 1
        szam = int(input("Kérek egy számot: "))
        if szam % 3 == 0:
            oszthato_szamok += 1
    print("3-al osztható számok: ", oszthato_szamok)

def harmadik():
    print("Harmadik feladat!")
    #Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
    szam = int(input("Kérek egy számot ami 10-el osztható: "))
    while not (szam % 10 == 0):
        szam = int(input("Kérek egy számot ami 10-el osztható: "))

def negyedik():
    print("Negyedik feladat!")
    #Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
    szam = int(input("Kérek egy számot ami kétjegyű és páros: "))
    while not ((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10))) and (szam % 2 == 0)):
        szam = int(input("Kérek egy számot ami kétjegyű és páros: "))


def otodik():
    print("Ötödik feladat!")
    #Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
    szam = int(input("Kérek egy pozitív páratlan számot: "))
    while not((szam > 0) and (szam % 2 == 1)):
        szam = int(input("Kérek egy pozitív páratlan számot: "))

def hatodik():
    print("Hatodik feladat!")
    #Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
    szam = int(input("Kérek egy számot ami 3-mal osztható vagy négyzetszám: "))
    while not(szam % 3 == 0 or szam ** 0.5 == 0):
        szam = int(input("Kérek egy számot ami 3-mal osztható vagy négyzetszám: "))


def hetedik():
    print("Hetedik feladat!")
    #Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
    i = 0
    while i < 1:
        szam1 = int(input("1Kérek egy számot: "))
        szam2 = int(input("2Kérek egy számot: "))
        szam3 = int(input("3Kérek egy számot: "))
        if szam1 + szam2 + szam3 == 180:
            i = 1
        else:
            szam1 = int(input("1Kérek egy számot: "))
            szam2 = int(input("2Kérek egy számot: "))
            szam3 = int(input("3Kérek egy számot: "))

def nyolcadik():
    print("Nyolcadik feladat!")
    #Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
    i = 0
    while i < 1:
        szoveg = input("Kérek egy legalább 3 betűs szót: ")
        if len(szoveg) >= 3:
            print(szoveg.upper())
            i = 1

def kilencedik():
    print("Kilencedik feladat!")
    #Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
    szoveg = input("Kérek egy szót ami csak kis betű és legalább 4 karakter: ")
    while not(len(szoveg) >= 4 and szoveg.islower()):
        szoveg = input("Kérek egy szót ami csak kis betű és legalább 4 karakter: ")
        print(szoveg)

def tizedik():
    print("Tizedik feladat!")
    #Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
    #A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!
    osszeg = 0
    db = 0
    i = 0

    while i < 1:
        szam = int(input("Kérlek, adj meg egy egész számot (0 a kilépéshez): "))
        if szam == 0:
            i = 1
        if szam < 0:
            szam = int(input("+Kérlek, adj meg egy egész számot (0 a kilépéshez): "))

        osszeg += szam
        db += 1

    if db > 0:
        atlag = osszeg / db
        print("Az adott számok átlaga:", atlag)
        print("Gratulálok nyereményed egy Gucci táska")
    else:
        print("Nem adtál meg egyetlen számot sem.")

