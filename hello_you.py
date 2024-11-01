# de main functie toont de hoofdfunctie. Je kunt met de main functie ook meerdere andere functies tegelijk volgen. Hiermee kan je het mooi verzamelen
# zie ook hello_you_expanded voor een uitgebreid voorbeeld van een combinatie van de verschillende functies onder de 'main' functie. 

def say_hello():
    your_name = input("What is your name? ")
    print("Hello, ", your_name, "!", sep="")

def main():
    say_hello()

main()

