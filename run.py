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

test = SHEET.worksheet('results')
data = test.get_all_values()
print(data)


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
# Output what is currentlt the most popular pet
# Display results as dictionary
# Total people surveyed
# Output to google sheet - should update graph also


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
