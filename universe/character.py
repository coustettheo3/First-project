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

print(creat_character())

print (creat_character())