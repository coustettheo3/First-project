import json
import os


def ask_text(message):
    user_input = ""
    while not user_input:
        raw_input = input(message)
        cleaned_input = raw_input.strip()
        if cleaned_input:
            user_input = cleaned_input
    return user_input


def ask_number(message, min_val=None, max_val=None):
    valid_number = False
    result = 0

    while not valid_number:
        user_input = input(message).strip()

        if not user_input:
            continue

        is_negative = False
        start_index = 0

        if user_input[0] == '-':
            is_negative = True
            start_index = 1

        if is_negative and len(user_input) == 1:
            print("Please enter a valid number.")
            continue

        is_valid_format = True
        calculated_value = 0
        i = start_index

        while i < len(user_input) and is_valid_format:
            char = user_input[i]
            if '0' <= char <= '9':
                digit = ord(char) - ord('0')
                calculated_value = calculated_value * 10 + digit
            else:
                is_valid_format = False
            i += 1

        if not is_valid_format:
            print("Please enter a valid number.")
            continue

        if is_negative:
            calculated_value = -calculated_value

        if min_val is not None and calculated_value < min_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue

        if max_val is not None and calculated_value > max_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue

        result = calculated_value
        valid_number = True

    return result


def ask_choice(message, options):
    print(message)
    index = 1
    for i in options:
        print(f"{index}. {i}")
        index += 1

    user_choice = ask_number("Your choice: ", 1, len(options))
    return options[user_choice - 1]


def load_file(file_path):
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(current_dir)
    full_path = os.path.join(root_dir, file_path)

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: The file {full_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {full_path} is not valid JSON.")
        return {}