
def creat_character():
    print("welcome to login your character")
    name = input("Enter a name :")
    last_name = input("Enter a last name :")
    print("Choose your attributes:")
    cour = int(input("Courage level (1-10) of your character's:" ))
    while cour > 10 or cour <0:
        cour = int(input("Courage level (1-10) of your character's:"))
    inte = int(input("Intelligence level (1-10) of your character's:"))
    while inte > 10 or inte <0:
        inte = int(input("Intelligence level (1-10) of your character's:"))
    loy = int(input("Loyalty level (1-10) of your character's: "))
    while  loy > 10 or loy <0:
        loy = int(input("Loyalty level (1-10) of your character's: "))
    amb = int(input("Ambition level (1-10): "))
    while amb > 10 or amb <0:
        amb = int(input("Ambition level (1-10): "))
    print(f"Welcome {name} {last_name}")

def receive_letter():
    print("An owl flies through the window, delivering a letter sealed with the"
        "Hogwarts crest..."
        "“Dear Student,"
        "We are pleased to inform you that you have been accepted to Hogwarts"
        "School of Witchcraft and Wizardry!”")
    print("Do you accept this invitation and go to Hogwarts?")
    print()
    print("choice 1. Yes, of course!")
    print()
    print("choice 2. No, I'd rather stay with Uncle Vernon...")
    print()
    choice = 0
    while choice != 1 and choice !=2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")
    print("ou tear up the letter, and Uncle Vernon cheers:"
        "“EXCELLENT! Finally, someone NORMAL in this house!”"
        "The magical world will never know you existed... Game over.")
def meet_hagrid():
    print("Hagrid: 'Hello Harry! I’m here to help you with your shopping on Diagon"
          "Alley.'")
    print()
    print("Do you want to follow Hagrid?")
    print()
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")
    print()
    print("Hagrid gently insists and takes you along anyway!")

def buy_supplies(character):
    print("Welcome to Diagon Alley!")
    print()
    """je nn'ai pas fais cette fonction
    refait, c'est relou"""


def start_chapter_1():
    creat_character()
    receive_letter()
    meet_hagrid()
    buy_supplies(character)
    print("You just finish the first chapter!")


