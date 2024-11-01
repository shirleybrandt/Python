# Exercise 5: Working with Files

# open file and read content in boys en girls apart. Bestand staat in de data map, dus die moet eerst worden opgeroepen
# resultaat van het openen van de bestanden 'girls' en 'boys' are assigned to 'f'
with open('data/1880-boys.txt') as f:
    boys = f.read()

with open('data/1880-girls.txt') as f:
    girls = f.read()

# om alles in 1x in comment mode te zetten dan ctrl + / ingedrukt houden
# print(boys)
# print('------')
# print(girls)

# samenvoegen van bovenstaande bestanden in 1 enkel bestand
with open('data/1880-all.txt', "w") as f:
    f.write(boys + "\n" + girls)

