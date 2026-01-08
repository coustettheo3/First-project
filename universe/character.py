
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

def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }
    return character

def display_character(character):
    print("\nCharacter profile:")
    for key, value in character.items():
        if isinstance(value, list):
            content = ", ".join(value) if value else ""
            print(f"{key}: {content}")
        elif isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"- {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

def add_item(character, key, item):
    if key in character and isinstance(character[key], list):
        character[key].append(item)
    else:
        print(f"Error: Impossible to add item to '{key}'.")
def modify_money(character, amount):
    character["Money"] += amount