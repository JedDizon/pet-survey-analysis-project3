## Intro

The Pet Surveyor Analysis Program is a Python-based tool designed to collect and analyze data about participants' pets. It allows users to input details about the types of pets they own or have owned, aggregates the data, and updates a Google Sheets worksheet to keep track of counts for each type of animal. 

The program can reset previous data, add new entries, and determine the most popular animal based on the current dataset. It's an easy-to-use tool for managing and visualizing pet-related survey data efficiently.

<IMAGE_OF_SITE>
<LINK>

---

## Program flow 

1. The user is welcomed to the program and displays current data.
2. The user is asked if they want to keep the current data or reset the values to 0.
3. After answering this, the program begins.
4. It first asks if the participant has a pet.
    a. if Y, the program continues.
    b. if N, the program ends.
5. It then asks what the animal is.
6. The user must state the animal under the following headings:
    a. DOG
    b. CAT
    c. FISH
    d. BIRD
    e. REPTILE
    f. SMALL MAMMAL
    g. INSECTS
    h. OTHER
7. The user is then prompted to answer if there are more animals to add.
    a. if Y, the user can state another animal.
    b. if N, the program ends.
8. Before the program ends, the resulting animal counts are displayed again along with the current most popular animal as a pet. 

—

## Features 

The Pet Surveyor Analysis Program provides a user-friendly way to collect, manage, and analyze data about pet ownership. Below are its key features:

### 1. User Input and Validation
Prompt-based interface to gather information about the user's pets.

Validates inputs to ensure only predefined animal types (DOG, CAT, FISH, etc.) are accepted.

Supports adding multiple animals in a single session.

### 2. Dynamic Data Management
Integrates with Google Sheets to store and update survey results in real time.

Automatically aggregates and updates animal counts in the worksheet.

Handles both new data entry and existing data updates without duplications.

### 3. Reset Functionality
Allows users to reset all worksheet data to zero before starting a new survey.

Ensures previous data does not interfere with new results.

### 4. Data Analysis
Identifies the animal type with the highest count in the dataset.

Prints a message if all counts are zero, ensuring meaningful feedback even in edge cases.

### 5. Robust Error Handling
Ensures invalid inputs are gracefully handled with clear error messages.

Warns users if they try to add animals not predefined in the system.

### 6. Readable Outputs
Displays meaningful messages to guide users through the program workflow.

Prints the current worksheet data and results after updates for transparency.

### 7. Scalable Design
Built with modular functions, making it easy to extend and adapt for future use cases.

Supports a variety of predefined animal categories, including:
    - DOG
    - CAT
    - FISH
    - BIRD
    - REPTILE
    - SMALL MAMMAL
    - INSECTS
    - OTHER


## Future features 

a. Paste in list of animals separated by comma.
b. Make the survey more versataille for collecting a wider range of values: can add in own headings to collect data for.

—

## Data model 

The Pet Surveyor Analysis Program uses a structured data model to handle user input, data storage, and updates. Below is an overview of the data model used in this program:

### 1. User Input Data

**Format:** A list of strings representing the types of animals entered by the user (e.g., ["DOG", "CAT", "FISH"]).

**Source:** Captured through user prompts during program execution.

**Validation:** Ensures that the input matches predefined categories such as DOG, CAT, FISH, BIRD, etc.


### 2. Google Sheets Data

**Worksheet Name:** results

**Structure:**
Header Row:
Column A: Animal
Column B: Count

Data Rows:
Rows store predefined animal categories (e.g., DOG, CAT, FISH) with their respective counts.

Example:

    Animal         Count
    DOG            3
    CAT            2
    FISH           0
    BIRD           1
    REPTILE        0
    SMALL MAMMAL   0
    INSECTS        0
    OTHER          0

### 3. In-Memory Data Representation

The program uses a dictionary to store and process worksheet data during runtime.

**Keys**: Animal types (e.g., "DOG", "CAT", "FISH").

**Values**: Integer values representing counts of each animal type.

Example:

    worksheet_data = {
        "DOG": 3,
        "CAT": 2,
        "FISH": 0,
        "BIRD": 1,
        "REPTILE": 0,
        "SMALL MAMMAL": 0,
        "INSECTS": 0,
        "OTHER": 0
    }

### 4. Processing Workflow

**Input Aggregation**: User inputs are aggregated using Python’s Counter class to count occurrences of each animal.

Example:

    input_data = ["DOG", "DOG", "CAT"]
    new_counts = Counter(input_data)  # Output: {"DOG": 2, "CAT": 1}

**Worksheet Update**: The program fetches the current worksheet values, combines them with the new counts, and writes the updated totals back to the worksheet.

### 5. Key Functions

**get_worksheet_values()**: Retrieves the current worksheet data into a dictionary for processing.

**update_survey_worksheet(data)**: Updates the worksheet by aggregating current and new data.

**reset_prev_data()**: Resets all counts in the worksheet to 0.
get_highest_count_animal(): Identifies the animal with the highest count in the dataset.

This data model enables the program to efficiently collect, validate, process, and update pet-related data while maintaining accuracy and usability.



—

## Testing

### Manual Testing

Below are the details of manual tests conducted to ensure functionality:

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Test Starts**   | Test starts | Test starts           | **Test starts** |



### Bugs 


### Solved
Bug1: While loop won’t end when answering “N” to if any more animals to add
	Fix: Removed Recursion in keep_asking(). Removed the recursive call what_animal() inside keep_asking(). Instead, what_animal() uses the return value of keep_asking() to decide whether to continue or stop.

Bug2: infinite loop. ask_to_reset_prev_data calls do_you_have_pets if the user chooses not to reset the data. do_you_have_pets completes and then continues back to main, which calls ask_to_reset_prev_data again.
	Fix: Add a return Value for ask_to_reset_prev_data (True / False), Removed do_you_have_pets() from ask_to_reset_prev_data. Streamlined main by calling ask_to_reset_prev_data once, handles the decision, and proceeds without loops.

### Remaining

Bug: Keep getting the below message in terminal if resetting previous values. Doesn't impact funtion of the program.

    /workspaces/pet-survey-analysis-project3/run.py:126: DeprecationWarning: The order of arguments in worksheet.update() has changed. Please pass values first and range_name secondor used named arguments (range_name=, values=)
    worksheet_to_update.update('B2:B9', [[0]] * 8)
    Previous data has been reset.

—

## Validator 

## PEP8 


— 

## Deployment 

### Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.


### Live link:

 Pet Survey Analysis! < SITE LINK >


--- 

## Credits

ChatGPT code
So that each upload to worksheet doesn’t create a new line and adds onto previous result

Find highest number
https://www.youtube.com/watch?v=BncMTg_7H8Q 
