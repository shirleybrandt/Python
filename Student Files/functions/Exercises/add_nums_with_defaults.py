# Exercise 7

# basis opgave. 
def add_nums(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)

def main():
    add_nums(1, 2, 0, 0, 0)
    add_nums(1, 2, 3, 4, 5)
    add_nums(11, 12, 13, 14, 0)
    add_nums(101, 201, 301, 0, 0)

main()


# doel van de opgave is om ervoor te zorgen dat de functie zowel 2, 3, 4 als 5 nummers bij elkaar kan optellen
# in bovenstaande opgave zul je zien dat een input als add_nums(1,2) niet werkt, omdat er 5 parameters worden verwacht en er maar 2 worden meegegeven
# je kunt dit oplossen door default values mee te geven aan de parameters, deze worden enkel meegegeven wanneer er geen andere parameters worden meegegeven
def add_nums(num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0):
    total = num1 + num2 + num3 + num4 + num5
    print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)

def main():
    add_nums(1, 2)
    add_nums(1, 2, 3, 4, 5)
    add_nums(11, 12, 13, 14)
    add_nums(101, 201, 301)

main()