import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

## Fő osztályok

## Járat (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
## BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
## NemzetkoziJarat: Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
## LégiTársaság: Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
## JegyFoglalás: A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.


class jarat:


class belfoldi_jarat:


class nemzetkozi_jarat:


class legi_tarsasag:


class jegy_foglalas:


## Felhasználói interfész

## Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
## Foglalás lemondása
## Jegy foglalása
## Foglalások listázása

def program(option):
    if option == '1':
        ## Foglalasi funkcio
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


## Funkciók

## Jegy foglalása: A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
## Foglalás lemondása: A felhasználó lemondhatja a meglévő foglalást.
## Foglalások listázása: Az összes aktuális foglalás listázása.

def jegy_foglalas():


def jegy_foglalas_lemondas():


def jegy_foglalasok_listazasa():


if __name__ == "__main__":
    while True:
        option = main_menu()
        program(option)
