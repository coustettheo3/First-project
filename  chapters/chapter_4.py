import random
from utils.input_utils import load_file
from universe.house import update_house_points
from universe.character import display_character


def create_team(house, team_data, is_player=False, player=None):
    team = {
        "name": house,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": []
    }

    house_data = team_data.get(house, {})
    raw_players = house_data.get("players", [])

    if is_player and player:
        full_name = f"{player['First Name']} {player['Last Name']}"
        player_entry = f"{full_name} (Seeker)"
        team["players"].append(player_entry)

        for p_str in raw_players:
            if "(Seeker)" not in p_str:
                team["players"].append(p_str)
    else:
        team["players"] = raw_players

    return team


def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal = random.randint(1, 10)

    if chance_goal >= 6:
        scorer = ""
        if player_is_seeker:
            scorer = attacking_team["players"][0]
        else:
            scorer = random.choice(attacking_team["players"])

        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
        print(f"{scorer} scores a goal for {attacking_team['name']}! (+10 points)")
    else:
        defending_team["goals_blocked"] += 1
        print(f"{defending_team['name']} blocks the attack!")


def golden_snitch_appears():
    chance = random.randint(1, 6)
    return chance == 6


def catch_golden_snitch(e1, e2):
    winner_index = random.randint(1, 2)
    winning_team = e1 if winner_index == 1 else e2

    winning_team["score"] += 150
    winning_team["caught_snitch"] = True

    return winning_team


def display_score(e1, e2):
    print("Current score:")
    print(f"â†’ {e1['name']}: {e1['score']} points")
    print(f"â†’ {e2['name']}: {e2['score']} points")


def display_team(house, team):
    print(f"{house} team:")
    for p in team["players"]:
        print(f"- {p}")


def quidditch_match(character, houses):
    team_data = load_file("data/teams_quidditch.json")
    player_house = character.get("House", "Gryffindor")

    available_houses = list(team_data.keys())
    if player_house in available_houses:
        available_houses.remove(player_house)
    opponent_house = random.choice(available_houses)

    print(f"Quidditch Match: {player_house} vs {opponent_house}!")

    player_team = create_team(player_house, team_data, is_player=True, player=character)
    opponent_team = create_team(opponent_house, team_data, is_player=False)

    display_team(player_house, player_team)
    print("")
    display_team(opponent_house, opponent_team)

    print(f"\nYou are playing for {player_house} as the Seeker")


    turns = 0
    match_over = False

    while turns < 20 and not match_over:
        turns += 1
        print(f"â”â”â” Turn {turns} â”â”â”")

        attempt_goal(player_team, opponent_team, player_is_seeker=True)
        attempt_goal(opponent_team, player_team, player_is_seeker=False)

        display_score(player_team, opponent_team)

        if golden_snitch_appears():
            winner_snitch = catch_golden_snitch(player_team, opponent_team)
            print(f"The Golden Snitch has been caught by {winner_snitch['name']}! (+150 points)")
            match_over = True

        if not match_over:
            input("Press Enter to continue")

    print("\nEnd of the match!")
    display_score(player_team, opponent_team)

    winner = None
    if player_team["score"] > opponent_team["score"]:
        winner = player_team
    elif opponent_team["score"] > player_team["score"]:
        winner = opponent_team

    if winner:
        print(f"Victory for {winner['name']}!")
        print(f"+500 points for {winner['name']}! Total: {winner['score']} points.")
        input("Press Enter to continue...")
        update_house_points(houses, winner['name'], 500)
        input("Press Enter to continue...")
    else:
        print("It's a draw!")


def start_chapter_4_quidditch(character, houses):
    print("\n=== Chapter 4: The Quidditch Match ===")
    quidditch_match(character, houses)
    print("\nEnd of Chapter 4 â€” What an incredible performance on the field!")
    display_character(character)