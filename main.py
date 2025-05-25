import os

## Fő osztályok

## Járat (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
## BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
## NemzetkoziJarat: Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
## LégiTársaság: Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
## JegyFoglalás: A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

#Osztaly: jarat()
#
#vars: jaratszam 
#- minden repter kap egy jaratszamot ami egy 3 jegyu szam,
# maga a jarat a kindulo illetve a celallomas szamjegyeinek osszeadasa alkot egy jaratot
# pl: Eger -> Vienna = BEL-1234 could also be for egKUL1725
#
#erkezo_repter
#
#indulo_repter
#- 
#
#DEFAULT jegyar (?)
#
#

class Jarat():
    #Ha az index paros akkor belfoldi, ha paratlan akkor kulfoldi
    kulfoldi_repterek = {"Vienna" : "VIE" , "Barcelona": "BCN", "Stockholm": "ARN"}
    belfoldi_repterek = {"Budapest": "BUD", "Debrecen": "DEB", "Miskolc": "MCQ"}

    def eval(kulfoldi_repterek, belfoldi_repterek, indulo_repter, erkezo_repter):

        if(indulo_repter in belfoldi_repterek and erkezo_repter in belfoldi_repterek):
            tipus = "BEL"
            return tipus
        else:
            tipus = "KUL"
            return tipus


        #repter_lista = list(repterek.values())
        
    #class belfoldi_jarat: 
class Belfoldi_jarat(Jarat):

    def belfoldi_jaratszam(tipus, indulo_repter, erkezo_repter):

        azonositok = {"Vienna" : 17, "Budapest" : 25, "Barcelona" : 31, "Debrecen" : 46, "Stockholm" : 59, "Miskolc" : 63}


        jaratszam = tipus + str(azonositok[indulo_repter]) + str(azonositok[erkezo_repter])

        return jaratszam

    #class kulfoldi_jarat: 
class Kulfoldi_jarat(Jarat):
        
    def kulfoldi_jaratszam(tipus, indulo_repter, erkezo_repter):

        azonositok = {"Vienna" : 17, "Budapest" : 25, "Barcelona" : 31, "Debrecen" : 46, "Stockholm" : 59, "Miskolc" : 63}

        jaratszam = tipus + azonositok[indulo_repter] + azonositok[erkezo_repter]

        return jaratszam #:)

    #class legi_tarsasag:
class Legi_tarsasag(Belfoldi_jarat, Kulfoldi_jarat):
        # azonosito = 
        # jaratok = []
        # legitarsasagok = {}

    def calculator(tipus, legitarsasag):
        legitarsasagok_belfold = {"RyanAir" : 0.78, "GDAir" : 0.8, "WizzAir" : 0.9}
        legitarsasagok_kulfold = {"RyanAir" : 1.1, "GDAir" : 1.115, "WizzAir" : 1.12}

        if(tipus == "BEL"):
            if(legitarsasag in legitarsasagok_belfold):
                ar = 40000
                ar = ar * legitarsasagok_belfold[legitarsasag]

                return ar
            else: print("vele nem tudsz levegozni a levegoben")
        else: 
            print("add meg kivel akarsz a levegoben levegozni")

            if(legitarsasag in legitarsasagok_kulfold):
                ar = 40000
                ar = ar * legitarsasagok_kulfold[legitarsasag]

                return ar
            else: print("vele nem tudsz levegozni a levegoben")


    #class jegy_foglalas:
class Jegy_foglalas(Jarat):

    def jegy_foglalas(self):
        
        indulo_repter = input()
        erkezo_repter = input()

        tipus = Jarat.eval(Jarat.kulfoldi_repterek, Jarat.belfoldi_repterek, indulo_repter, erkezo_repter)

        if(tipus == "BEL"):
            jaratszam = Belfoldi_jarat.belfoldi_jaratszam(tipus, indulo_repter, erkezo_repter)
        else:
            jaratszam = Kulfoldi_jarat.kulfoldi_jaratszam(tipus, indulo_repter, erkezo_repter)
        
        print("add meg kivel akarsz a levegoben levegozni")
        legitarsasag = input()


        ar = Legi_tarsasag.calculator(tipus, legitarsasag)

        print(indulo_repter + " " + erkezo_repter + " " + jaratszam + " " + str(ar))

        


    #def jegy_foglalas_lemondas(azonosito):


    #def jegy_foglalasok_listazasa(foglalas):


## Felhasználói interfész

## Egyszerű felhasználói interfész, amely opciokent lehetővé teszi a következő műveleteket:
## Foglalás lemondása
## Jegy foglalása
## Foglalások listázása

## Funkciók

## Jegy foglalása: A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
## Foglalás lemondása: A felhasználó lemondhatja a meglévő foglalást.
## Foglalások listázása: Az összes aktuális foglalás listázása.

class main_menu():

    def program(option):

        if option == '1':
            ## Foglalasi funkcio
            foglalas = Jegy_foglalas()
            foglalas.jegy_foglalas()   
        elif option == '2':
            ## Lemondasi funkcio
            print("meg olyan nincse")
        elif option == '3':
            ## Listazasi funkcio 
            print("meg olyan nincse")
        elif option == '9':
            print("A program bezárása...")
            exit()
        else:
            print("Helytelen menüpont, fussunk neki megegyszer!")
            input("\nNyomjon Entert a folytatáshoz...")

    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


## Felhasználói interfész

## Egyszerű felhasználói interfész, amely opciokent lehetővé teszi a következő műveleteket:
## Foglalás lemondása
## Jegy foglalása
## Foglalások listázása

## Funkciók

## Jegy foglalása: A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
## Foglalás lemondása: A felhasználó lemondhatja a meglévő foglalást.
## Foglalások listázása: Az összes aktuális foglalás listázása.


if __name__ == "__main__":
    while True:
        print ("valassz opciot")
        option = input()

        main_menu.program(option)
