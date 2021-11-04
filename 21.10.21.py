def feladat24():
    szam=float(input("kérek egy számot: "))
    while szam!=0:
        szam=float(input("kérek egy másik számot! Kilépés: 0"))

def feladat25():
    szam=float(input("kérek egy pozitiv számot: "))
    while szam<=0:
        szam=float(input("nem pozitiv számot adtál,add meg ujra: "))

def feladat26():
    szam=float(input("kérek egy számot: "))
    while szam <10: 
        szam=float(input("a szam nagyobb mint 10"))
        osszeg+=szam
    print("a beadott szamok osszege",osszeg)

#itt kezodik a főprogram
#feladat24()
#feladat25()
feladat26()