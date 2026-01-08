from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from chapters.chapter_4 import start_chapter_4_quidditch
from utils.input_utils import ask_choice





def display_main_menu():
    print("Harry Potter")
def launch_menu_choice():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    game_running = True

    while game_running:

        display_main_menu()
        choice = ask_choice("Your choice:", ["Start Adventure", "Exit"])

        if choice == "Start Adventure":
            character = start_chapter_1()
            start_chapter_2(character)
            start_chapter_3(character, houses)
            start_chapter_4_quidditch(character, houses)
            bonus_choice = ask_choice("Do you want to play the Secret Chapter (Chamber of Secrets)?", ["Yes", "No"])
            game_running = False
        elif choice == "Exit":
            print("Goodbye!")
            game_running = False