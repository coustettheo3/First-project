from utils.input_utils import ask_text, load_file
from universe.character import add_item, display_character
from universe.house import update_house_points, display_winning_house
import random


def learn_spells(character, file_path="data/spells.json"):
    print("\nYou begin your magic lessons at Hogwarts...")
    spells_data = load_file(file_path)

    offensive = []
    defensive = []
    utility = []

    for spell in spells_data:
        if spell["type"] == "Offensive":
            offensive.append(spell)
        elif spell["type"] == "Defensive":
            defensive.append(spell)
        elif spell["type"] == "Utility":
            utility.append(spell)

    learned_spells = []

    s1 = random.choice(offensive)
    learned_spells.append(s1)

    s2 = random.choice(defensive)
    learned_spells.append(s2)

    while len(learned_spells) < 5:
        s = random.choice(utility)
        if s not in learned_spells:
            learned_spells.append(s)

    for spell in learned_spells:
        add_item(character, "Spells", spell["name"])
        print(f"You have just learned the spell: {spell['name']} ({spell['type']})")
        input("Press Enter to continue...")

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for spell in learned_spells:
        print(f"- {spell['name']} ({spell['type']}): {spell['description']}")


def magic_quiz(character, file_path="data/magic_quiz.json"):
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")

    questions_data = load_file(file_path)
    selected_questions = []

    while len(selected_questions) < 4:
        q = random.choice(questions_data)
        if q not in selected_questions:
            selected_questions.append(q)

    score = 0
    i = 1
    for item in selected_questions:
        print(f"{i}. {item['question']}")
        user_answer = ask_text("> ")

        if user_answer.strip().lower() == item['answer'].strip().lower():
            print("Correct answer! +25 points for your house.")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {item['answer']}")
        i += 1

    print(f"Score obtained: {score} points")
    return score


def start_chapter_3(character, houses):
    learn_spells(character)
    points = magic_quiz(character)

    user_house = character.get("House")
    if user_house:
        update_house_points(houses, user_house, points)

    display_winning_house(houses)
    display_character(character)