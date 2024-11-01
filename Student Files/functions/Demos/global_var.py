# Demo 2.3 

# Je hebt hier twee keer de variable x gedefinieerd. Echter, is de ene x = 0 een 'global' variable (deze zit buiten de functie), en de x = 1 (die wordt getoond binnen de functie) is local 
# dit zijn dus twee verschillende variabelen
# normaal gesproken kan je geen twee variabelen hebben met dezelfde naam
# de get_x() verwijst naar de global variable (x = 0) en de set_x() verwijst naar de local variable (x=1) en die laatste bestaat dus niet buiten deze functie. 

x = 0

def set_x():
    x = 1
    print("from set_x():", x)

def get_x():
    print("from get_x():", x)

def main():
    set_x()
    get_x()

main()