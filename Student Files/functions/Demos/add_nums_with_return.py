# Demo 2.7

# het return statement wordt hier gebruikt om het print statement 'uit te stellen'
# het resultaat van add_nums wordt hier 'bewaard' om er later opnieuw iets mee te gaan doen. In dit geval optellen van nummers gebruikmakend van de uitkomst van de eerdere sommen

def add_nums(num1, num2, num3=0, num4=0, num5=0):
    total = num1 + num2 + num3 + num4 + num5
    return total

def main():
    result = add_nums(1, 2)
    print(result)
    result = add_nums(result, 3)
    print(result)
    result = add_nums(result, 4)
    print(result)
    result = add_nums(result, 5)
    print(result)
    result = add_nums(result, 6)
    print(result)

main()