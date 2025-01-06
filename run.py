import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pet_survey_analysis')

# test = SHEET.worksheet('results')
# data = test.get_all_values()
# print(data)

def do_you_have_pets():
    """
    Get pet data input from user
    """
    while True:
        question_one = input("Does the participant have / had a pet? (Y / N)\n").strip().upper()
        print(f"User input is {question_one}\n")
        
        if validate_y_n_question(question_one):
            if question_one == 'N':
                print("No pets, program will end.")
                return "No" # answered_no (Need to be defined) 
            elif question_one == "Y":
                print("Data is valid!")
                what_animal()
                break
    return question_one


def validate_y_n_question(answer):
    """
    Validate answer given.
    Checks if answer given was Y or N.
    """    
    try:
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
    while True:
        question_two = input("What animal?\n").strip().upper()
        print(f"User input is {question_two}\n")
        if validate_what_animal(question_two):
            print("Animal is valid!")
            if not keep_asking():
                break
    return question_two

def validate_what_animal(answer):
    """
    Validate answer given.
    Checks if answer given was DOG, CAT, FISH, BIRD, OTHER.
    """
    try:
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
        print(f"User input is {question_three}\n")
        if validate_y_n_question(question_three):
            if question_three == 'N':
                print("No additional animals to add")
                return False
            elif question_three == "Y":
                print("You want to add more animals")
                return True


def validate_another_pet(answer):
    """
    Validate answer given.
    Checks if answer given was Y or N.
    """
    try:
        if answer not in ('Y', 'N'):
            raise ValueError(
                f"Y or N is required, you answered {answer}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


print("Welcome to Pet Surveyor Analysis\n")
question_one_data = do_you_have_pets()



# Plan
# Welcome user to Pet Surveyor Analysis, Input function (Does participant have / had a pet) - Y/N?
# NO - keep track of result as NoPet
# YES - To next prompt; What animal?
#       Validate not numbers
#       Check for most popular animals 
#           (DOG, CAT, FISH, BIRD, REPTILE / AMPHIBIAN, SMALL MAMMAL (i.e. Hamster, Mouse), INSECTS, OTHER
#       If not in the list, goes under "OTHER"
# LOOP - what animal - continue? 
# Output what is currentlt the most popular pet
# Display results as dictionary
# Total people surveyed
# Output to google sheet - should update graph also
#add clear prev data option at start


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
