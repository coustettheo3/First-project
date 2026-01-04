from utils.input_utils import ask_choice


def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
        print(f"Points update: {house_name} {points:+d} points.")
        print(f"New total for {house_name}: {houses[house_name]}")
    else:
        print(f"Warning: House '{house_name}' does not exist.")


def display_winning_house(houses):
    max_score = -1
    for score in houses.values():
        if score > max_score:
            max_score = score

    winners = []
    for name, score in houses.items():
        if score == max_score:
            winners.append(name)

    print(f" The leading house is: {', '.join(winners)} with {max_score} points!")


def assign_house(character, questions):
    scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    attributes = character["Attributes"]
    scores["Gryffindor"] += attributes["courage"] * 2
    scores["Slytherin"] += attributes["ambition"] * 2
    scores["Hufflepuff"] += attributes["loyalty"] * 2
    scores["Ravenclaw"] += attributes["intelligence"] * 2

    for question_text, options, houses_order in questions:
        choice_text = ask_choice(question_text, options)
        index = options.index(choice_text)
        chosen_house = houses_order[index]
        scores[chosen_house] += 3

    print("\nSummary of scores:")
    for house, score in scores.items():
        print(f"{house}: {score} points")

    best_house = ""
    highest_score = -1

    for house, score in scores.items():
        if score > highest_score:
            highest_score = score
            best_house = house

    return best_house