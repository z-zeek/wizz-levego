import os

## Fő osztályok

## Járat (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
## BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
## NemzetkoziJarat: Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
## LégiTársaság: Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
## JegyFoglalás: A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

class main_menu():

    def init_foglalas():
        #does txt exist?
        #if no:
        #   - create and populate sample jaratok
        #
        #if yes:
        #   - load it in

    def program(option):
        if option == '1':
            ## Foglalasi funkcio
            Jegyfoglalas.jegy_foglalas
        elif option == '2':
            ## Lemondasi funkcio
        elif option == '3':
            ## Listazasi funkcio 
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


#Osztaly: jarat()
#
#vars: jaratszam 
#- minden repter kap egy jaratszamot ami egy 3 jegyu szam,
# maga a jarat a kindulo illetve a celallomas szamjegyeinek osszeadasa alkot egy jaratot
# pl: Eger -> Vienna = 178250 (maybe 178-250), could also be startAirportLetters1725
#
#celallomas
#- 
#
#jegyar
#
#

    class Jarat():
        azonositok = [17, 25, 31, 46, 59, 63 ,75 , 82 , 94 , 10, 11]

        #Ha az index paros akkor belfoldi, ha paratlan akkor kulfoldi
        repterek = {"Vienna" : "VIE" , "Budapest": "BUD", "Barcelona": "BCN", "Debrecen": "DEB", "Stockholm": "ARN", "Miskolc": "MCQ"}

        print(x["name"])

        repter_lista = list(repterek.values())
        
    #class belfoldi_jarat: 
    class Belfoldi_jarat(Jarat):
        def __init__(self, azonosito, repterek):
            #super().__init__(fname, lname)  init(name, lname)
            self.azonosito = azonosito
            self.repterek = repterek

    

        belfoldi_azon = azonosito

    #class nemzetkozi_jarat: 
    class Nemzetkozi_jarat(Jarat):
            # azonosito = 
            # nemzetkozi_azonosito =

    #class legi_tarsasag:
    class Legi_tarsasag(Belfoldi_jarat, Nemzetkozi_jarat):
            # azonosito = 
            # jaratok = []

    #class jegy_foglalas:
    class Jegy_foglalas(Jarat):
        def __init__(self, azonosito):
            #super().__init__(fname, lname)  init(name, lname)
            self.azonosito = azonosito 
        

        def jegy_foglalas(azonosito, ar):


        def jegy_foglalas_lemondas(azonosito):


        def jegy_foglalasok_listazasa(foglalas):


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
        option = main_menu()
        program(option)
