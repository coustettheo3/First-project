from utils.input_utils import ask_choice, load_file
from universe.house import assign_house
from universe.character import display_character

def meet_friends(character):
    print("\nYou board the Hogwarts Express. The train slowly departs northward...")

    print("\nA red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")

    options_ron = ["Sure, have a seat!", "Sorry, I prefer to travel alone."]
    choice_ron = ask_choice("How do you respond?", options_ron)

    if choice_ron == "Sure, have a seat!":
        character["Attributes"]["loyalty"] += 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        character["Attributes"]["ambition"] += 1
        print("Ron shrugs and leaves to find another seat.")

    print("\nA girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")

    options_hermione = ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."]
    choice_hermione = ask_choice("How do you respond?", options_hermione)

    if choice_hermione == "Yes, I love learning new things!":
        character["Attributes"]["intelligence"] += 1
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else:
        character["Attributes"]["courage"] += 1
        print("Hermione looks slightly disappointed but nods.")

    print("\nThen a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")

    options_draco = ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."]
    choice_draco = ask_choice("How do you respond?", options_draco)

    if choice_draco == "Shake his hand politely.":
        character["Attributes"]["ambition"] += 1
    elif choice_draco == "Ignore him completely.":
        character["Attributes"]["loyalty"] += 1
    else:
        character["Attributes"]["courage"] += 1
        print("Draco frowns, annoyed. — You'll regret that!")

    print("\nThe train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!")
    print(f"Your updated attributes: {character['Attributes']}")


def welcome_message():
    print("\nYou arrive at the castle. Professor Dumbledore stands before the students.")
    print(
        "“Welcome to a new year at Hogwarts! Before the banquet begins, I would like to say a few words. And here they are: Nitwit! Blubber! Oddment! Tweak!”")
    input("Press Enter to continue...")


def sorting_ceremony(character):
    print("\nThe sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:")

    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends",
             "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    house = assign_house(character, questions)
    character["House"] = house

    print(f"\nThe Sorting Hat exclaims: {house}!!!")
    print(f"You join the {house} students to loud cheers!")


def enter_common_room(character):
    print("\nYou follow the prefects through the castle corridors...")
    houses_data = load_file("data/houses.json")
    user_house = character.get("House")

    if user_house in houses_data:
        info = houses_data[user_house]
        emoji = info.get("emoji", "")
        print(f"{emoji} {info['description']}")
        print(f"{info.get('installation_message', 'Welcome!')}")

        colors = info.get("colors", [])
        if isinstance(colors, list):
            print(f"Your house colors: {', '.join(colors)}")
        else:
            print(f"Your house colors: {colors}")
    else:
        print("Error: House information not found.")


def start_chapter_2(character):
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)

    print("\n--- End of Chapter 2 ---")
    display_character(character)
    print("Classes are about to begin!")


