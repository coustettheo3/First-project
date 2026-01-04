import json

from utils.input_utils import load_file



def ask_number(text, min_val, max_val):
    choice = 0
    while choice < min_val or choice > max_val:
        try:
            choice = int(input(text))
        except ValueError:
            choice = 0
    return choice


def modify_money(character, amount):
    if "Money" not in character:
        character["Money"] = 0
    character["Money"] += amount


def add_item(character, key, item_name):
    if key not in character:
        character[key] = []

    character[key].append(item_name)


def display_character(character):
    print("\n=== YOUR CHARACTER ===")
    print(f"Name: {character.get('Name', '')} {character.get('LastName', '')}")
    print(f"Money: {character.get('Money', 0)} Galleons")
    print(f"Inventory: {character.get('Inventory', [])}")
    print("======================\n")


def creat_character():
    global character
    print("welcome to login your character")
    name = input("Enter a name :")
    last_name = input("Enter a last name :")
    print("Choose your attributes:")
    cour = int(input("Courage level (1-10) of your character's:" ))
    while cour > 10 or cour < 0:
        cour = int(input("Courage level (1-10) of your character's:"))
    inte = int(input("Intelligence level (1-10) of your character's:"))
    while inte > 10 or inte < 0:
        inte = int(input("Intelligence level (1-10) of your character's:"))
    loy = int(input("Loyalty level (1-10) of your character's: "))
    while loy > 10 or loy < 0:
        loy = int(input("Loyalty level (1-10) of your character's: "))
    amb = int(input("Ambition level (1-10): "))
    while amb > 10 or amb < 0:
        amb = int(input("Ambition level (1-10): "))
    print(f"Welcome {name} {last_name}")

    character = {
        "Name": name,
        "LastName": last_name,
        "Courage": cour,
        "Intelligence": inte,
        "Loyalty": loy,
        "Ambition": amb,
        "Money": 50,      # tu peux mettre la somme que tu veux
        "Inventory": []
    }


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
    while choice != 1 and choice != 2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")

    if choice == 2:
        print("You tear up the letter, and Uncle Vernon cheers:"
            "“EXCELLENT! Finally, someone NORMAL in this house!”"
            "The magical world will never know you existed... Game over.")



def meet_hagrid():
    print("Hagrid: 'Hello Harry! I’m here to help you with your shopping on Diagon"
          "Alley.'")
    print()
    print("Do you want to follow Hagrid?")
    print()
    print("choice 1. Yes")
    print("choice 2. No")
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Enter your choice (1;2)"))
    print(f"Your choice : {choice}")
    print()
    print("Hagrid gently insists and takes you along anyway!")


def buy_supplies(character):
    print("\nWelcome to Diagon Alley!")

    raw_data = load_file("data/inventory.json")

    # si load_file renvoie un chemin, on lit le json ici
    if isinstance(raw_data, str):
        try:
            with open(raw_data, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
        except Exception:
            print("Error: Cannot open inventory.json. Check load_file and file path.")
            return
    items_catalog = {}

    for value in raw_data.values():
        if isinstance(value, list) and len(value) >= 2:
            name = value[0]
            price = value[1]
            items_catalog[name] = price

    pets_catalog = {
        "Owl": 20,
        "Cat": 15,
        "Rat": 10,
        "Toad": 5
    }

    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]

    while len(required_items) > 0:
        print("\nCatalog of available items:")
        item_list = list(items_catalog.keys())


        index = 1
        for name in item_list:
            price = items_catalog[name]
            req_mark = "(required)" if name in required_items else ""
            print(f"{index}. {name} - {price} Galleons {req_mark}")
            index += 1

        print(f"You have {character['Money']} Galleons.")
        print(f"Remaining required items: {', '.join(required_items)}")

        choice_index = ask_number("Enter the number of the item to buy: ", 1, len(item_list))
        item_name = item_list[choice_index - 1]
        price = items_catalog[item_name]

        if character["Money"] >= price:
            modify_money(character, -price)
            add_item(character, "Inventory", item_name)
            print(f"You bought: {item_name} (-{price} Galleons).")

            if item_name in required_items:
                required_items.remove(item_name)


    print("All required items have been purchased!")
    print("It's time to choose your Hogwarts pet!")
    print(f"You have {character['Money']} Galleons.")

    print("Available pets:")
    pet_list = list(pets_catalog.keys())
    index = 1
    for name, price in pets_catalog.items():
        print(f"{index}. {name} - {price} Galleons")
        index += 1

    choice_index = ask_number("Which pet do you want? ", 1, len(pet_list))
    pet_name = pet_list[choice_index - 1]
    pet_price = pets_catalog[pet_name]

    if character["Money"] >= pet_price:
        modify_money(character, -pet_price)
        add_item(character, "Inventory", pet_name)
        print(f"You chose: {pet_name} (-{pet_price} Galleons).")


    print("All required items have been successfully purchased! Here is your final inventory:")
    display_character(character)


def start_chapter_1():
    creat_character()
    receive_letter()
    meet_hagrid()
    buy_supplies(character)
    print("You just finish the first chapter!")