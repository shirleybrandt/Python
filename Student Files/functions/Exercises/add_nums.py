# Exercise 6

# Deze moeten worden aangepast naar een meer logische en flexibele oplossing om twee getallen bij elkaar op te tellen
def add_3_and_6():
    total = 3 + 6
    print('3 + 6 = ', total)

def add_10_and_12():
    total = 10 + 12
    print('10 + 12 = ', total)

def main():
    add_3_and_6()
    add_10_and_12()

main()

# oplossing Shirley
# in eerste instantie werkte het niet, omdat de nummers worden gezien als str. Deze moeten dus eerst worden omgezet naar int. 
def add_nums():
    num1 = input('Put in the first number: ')
    num2 = input('Put in the second number: ')
    total = str(int(num1) + int(num2))
    print(num1 + " + " + num2 + " = " + total)

add_nums()

# oplossing vanuit het boek
def add_nums(num1, num2):
    total = num1 + num2
    print(num1, '+', num2, '=', total)

def main():
    add_nums(3,6)
    add_nums(10,12)
    add_nums('q','a')

main()


# Het blijkt dat deze functie ook werkt op een manier die wij niet willen, namelijk dat ook letters of symbolen bij elkaar worden opgeteld (achter elkaar geplakt)
# Dit kun je oplossen door de input geforceerd om te zetten naar een int. In het geval van een string kan dit niet, dus geeft hij een foutmelding. Dit is wat we willen
def add_nums(num1, num2):
    total = int(num1) + int(num2)
    print(num1, '+', num2, '=', total)

def main():
    add_nums(3,6)
    add_nums(10,12)
    add_nums('q','a')

main()


# als je geen parameters / argumenten meegeeft dan zie je dat de functie niet werkt. Om dat te omzeilen, kan je ervoor kiezen een default  waarde toe te voegen zodat de functie blijft werken
# deze default waarde wordt dus alleen gebruikt op het moment dat er geen andere parameters worden meegegeven.

def add_nums(num1 = 0, num2 = 0):
    total = int(num1) + int(num2)
    print(num1, '+', num2, '=', total)

def main():
    add_nums(3,6)
    add_nums(10,12)
    add_nums()

main()