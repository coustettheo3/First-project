def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward..."
        "A red-haired boy enters your compartment, looking friendly.")
    print("- Hi! I'm Ron Weasley. Mind if I sit with you?")
    print()
    print("How do you respond?")
    print()
    print("1. Sure, have a seat!")
    print()
    print("2. Sorry, I prefer to travel alone.")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")
    print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    print()
    print()
    print("A girl enters next, already carrying a stack of books.")
    print("- Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print()
    print("How do you respond?")
    print()
    print("1. Yes, I love learning new things!")
    print()
    print("2. Uh… no, I prefer adventures over books.")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")
    print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    print()
    print()
    print("Then a blonde boy enters, looking arrogant.")
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the"
        "start, don't you think?")
    print()
    print("How do you respond?")
    print()
    print("1. Shake his hand politely.")
    print()
    print("2. Ignore him completely.")
    print()
    print("3. Respond with arrogance.")
    choice = 0
    while choice != 1 and choice != 2 and choice !=3:
        choice = int(input("Enter your choice (1;2;3)"))
    print(f"Your choice : {choice}")
    print("Then a blonde boy enters, looking arrogant.")

def welcome_message():
    return "Welcome in Hogward!!!"

def sorting_ceremony(character):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm"
             "and observe"],
             ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and"
             "hardworking", "Intelligent and curious"],
             ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best"
             "strategy", "Rely on your friends",
                                             "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]


def enter_common_room(character):
    print("You follow the prefects through the castle corridors..."
    "🐍 You discover a vaulted common room, illuminated by the green glow"
    "of the lake. Students watch you with curiosity and respect."
    "✨ ✨ Cunning and ambition are your allies. Welcome to the noble House"
    "of Slytherin."
    f"Your house colors:{colors}")""

def start_chapter_2(character):
    meet_friends(character)
    welcome_message()
    orting_ceremony(character)
    enter_common_room(character)
    print(" You finish Chapter 2")


