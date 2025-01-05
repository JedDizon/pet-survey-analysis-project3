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
        
        if validate_do_you_have_pets(question_one):
            if question_one == 'N':
                print("No pets, program will end.")
                return "No" # answered_no (Need to be defined) 
            elif question_one == "Y":
                print("Data is valid!")
                break
    return question_one_answer


def validate_do_you_have_pets(answer):
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

    # Validate result
    # Ensure key pressed is Y or N - capitalize answer
    # Else - error message and restart question


print("Welcome to Pet Surveyor Analysis\n")
question_one_data = do_you_have_pets()

# Idea1
# Welcome user to Pet Surveyor Analysis, Input function (how many have no pets) 
# Input continue; how many have (Dog, cat, fish, bird, other)
#       Validate checks for integers, not negative, not points, not characters
# Output what is most popular pet
# Display results as dictionary
# Output to google sheet - should update graph also
#
#
#
# Idea2
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


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
