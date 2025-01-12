import gspread
from google.oauth2.service_account import Credentials
from collections import Counter


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pet_survey_analysis')


def do_you_have_pets():
    """
    Get pet data input from user
    """
    while True:
        question_one = input("Does the participant have / had a pet? (Y / N)\n").strip().upper()

        if not question_one:
            print("Input cannot be empty. Please enter Y or N.\n")
            continue

        if validate_y_n_question(question_one):
            if question_one == 'N':
                print("No pets, program will end.")
                return []
            elif question_one == "Y":
                return what_animal()
    return question_one


def validate_y_n_question(answer):
    """
    Validate answer given.
    Checks if answer given was Y or N.
    """
    try:
        if not answer:
            raise ValueError("Input cannot be empty.")
        if answer not in ('Y', 'N'):
            raise ValueError(
                f"Y or N is required, you answered {answer}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def what_animal():
    """
    Get pet data input from user
    """
    animal_list = []
    while True:
        print("Choose an animal under the following headings:")
        print("DOG, CAT, FISH, BIRD, REPTILE, SMALL MAMMAL, INSECTS, or OTHER")
        question_two = input("What animal?\n").strip().upper()

        if not question_two:
            print("Input cannot be empty. Please enter a valid animal.\n")
            continue

        if validate_what_animal(question_two):
            print("Animal is valid!")
            animal_list.append(question_two)
            if not keep_asking():
                break
    return animal_list


def validate_what_animal(answer):
    """
    Validate answer given.
    Checks if answer given was DOG, CAT, FISH, BIRD, OTHER.
    """
    try:
        if not answer:
            raise ValueError("Input cannot be empty.")
        if answer not in ('DOG', 'CAT', 'FISH', 'BIRD', 'REPTILE', 'SMALL MAMMAL', 'INSECTS', 'OTHER'):
            raise ValueError(
                f"DOG, CAT, FISH, BIRD, REPTILE, SMALL MAMMAL, INSECTS or OTHER is required, you answered {answer}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def keep_asking():
    """
    Ask user if they have another animal to input
    """
    while True:
        question_three = input("Do you have another animal to add? (Y / N)\n").strip().upper()

        if validate_y_n_question(question_three):
            if question_three == 'N':
                print("No additional animals to add")
                return False
            elif question_three == "Y":
                print("You want to add more animals")
                return True


def ask_to_reset_prev_data():
    """
    Ask if user wants to reset previous data from worksheet.
    """
    while True:
        question_four = input("Do you want to clear previous data? (Y / N)\n").strip().upper()

        if validate_y_n_question(question_four):
            if question_four == 'N':
                print("Previous data will not be reset.")
                return False
            else:
                print("Previous data will be reset.")
                reset_prev_data()
                return True


def reset_prev_data():
    """
    Reset data back to 0 in the worksheet.
    """
    print("Resetting previous data...\n")
    worksheet_to_update = SHEET.worksheet("results")

    # Explicitly use named arguments to match the updated API (ChatGPT)
    worksheet_to_update.update(range_name='B2:B9', values=[[0]] * 8)

    # worksheet_to_update.update('B2:B9', [[0]] * 8) (ChatGPT)
    print("Previous data has been reset.\n")


def update_survey_worksheet(data):
    """
    Update survey worksheet with aggregated animal counts.
    """
    print("Updating survey worksheet...\n")

    # Get current worksheet values as a dictionary
    worksheet_data = get_worksheet_values()

    # Count new occurrences of each animal from the current data
    new_counts = Counter(data)

    # Update worksheet data with new counts
    for animal, count in new_counts.items():
        if animal in worksheet_data:
            worksheet_data[animal] += count
        else:
            print(f"Warning: {animal} is not listed in the worksheet. Skipping.")

    # Simulate worksheet update by printing (ChatGPT)
    # Start from row 2 to skip header
    for row_index, (animal, count) in enumerate(worksheet_data.items(), start=2):
        print(f"Updating worksheet: {animal} -> {count}")
        # Uncomment below line for actual worksheet update
        SHEET.worksheet("results").update_cell(row_index, 2, count)

    print("Survey worksheet updated successfully.\n")


def get_worksheet_values():
    """
    Get values from the 'results' worksheet and return as a dictionary.
    """
    print("Getting worksheet values...\n")
    results_worksheet = SHEET.worksheet("results")

    # Get all values from the worksheet
    data = results_worksheet.get_all_values()

    # Skip the header row and build a dictionary of Animal: Count
    worksheet_data = {row[0].strip().upper(): int(row[1]) for row in data[1:] if len(row) == 2}

    print(f"Current data: {worksheet_data}\n")
    return worksheet_data


def get_highest_count_animal():
    """
    Determine the most popular animal(s).
    If multiple animals have the same highest count, all are returned.
    """
    print("Determining the animal(s) with the highest count...\n")

    # Get the current worksheet data
    worksheet_data = get_worksheet_values()

    if all(count == 0 for count in worksheet_data.values()):
        print("All animal counts are 0. No highest count animal.\n")
        return None

    # Find the maximum count
    highest_count = max(worksheet_data.values())

    # Find all animals with the maximum count
    highest_animals = [animal for animal, count in worksheet_data.items() if count == highest_count]

    if len(highest_animals) > 1:
        print(f"Tie! The animals with the highest count ({highest_count}) are: {', '.join(highest_animals)}.\n")
    else:
        print(f"The animal with the highest count is '{highest_animals[0]}' with a count of {highest_count}.\n")

    return highest_animals, highest_count


def main():
    """
    Run all program functions
    """
    print("Welcome to Pet Surveyor Analysis\n")
    get_worksheet_values()
    data_reset = ask_to_reset_prev_data()

    animal_list = do_you_have_pets()
    print(f"Resulting animal list: {animal_list}")
    update_survey_worksheet(animal_list)
    get_highest_count_animal()

    print("Thank you for using Pet Surveyor Analysis! Your responses have been recorded.")


main()
