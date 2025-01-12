## Intro

The Pet Surveyor Analysis Program is a Python-based tool designed to collect and analyze data about participants' pets. It allows users to input details about the types of pets they own or have owned, aggregates the data, and updates a Google Sheets worksheet to keep track of counts for each type of animal. 

The program can reset previous data, add new entries, and determine the most popular animal based on the current dataset. It's an easy-to-use tool for managing and visualizing pet-related survey data efficiently.


[Pet Survey Analysis - Program](https://pet-survey-analysis-project3-dc2d0651f524.herokuapp.com) 


[Pet Survey Analysis - Worksheet](https://docs.google.com/spreadsheets/d/1C_0NYb2zTn44TahjGgOV47mYidhFjdlgo7ksUgCxE6U/edit?usp=sharing) 


![Website image](/assets/images/petsurveyanalysis-site-image.png)


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


## Features 

The Pet Surveyor Analysis Program provides a user-friendly way to collect, manage, and analyze data about pet ownership. Below are its key features:

### 1. User Input and Validation
Prompt-based interface to gather information about the user's pets.

Validates inputs to ensure only predefined animal types (DOG, CAT, FISH, etc.) are accepted.

Supports adding multiple animals in a single session.

![Pet choices](/assets/images/petsurveyanalysis-animal-choices.png)

### 2. Dynamic Data Management
Integrates with Google Sheets to store and update survey results in real time.

Automatically aggregates and updates animal counts in the worksheet.

Handles both new data entry and existing data updates without duplications.

![Google Sheets Integration](/assets/images/petsurveyanalysis-petsurvey-analysis-worksheet.png)

### 3. Reset Functionality
Allows users to reset all worksheet data to zero before starting a new survey.

Ensures previous data does not interfere with new results.

![Clear previous choices](/assets/images/petsurveyanalysis-clear-prev-data.png)

### 4. Data Analysis
Identifies the animal type with the highest count in the dataset.

Prints a message if all counts are zero, ensuring meaningful feedback even in edge cases.

![Highest Animal Count](/assets/images/petsurveyanalysis-highest-animal-count.png)

### 5. Robust Error Handling
Ensures invalid inputs are gracefully handled with clear error messages.

Warns users if they try to add animals not predefined in the system.

![Error Message](/assets/images/petsurveyanalysis-animal-validation.png)

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

### 1. Advanced Analytics and Visualization
Generate charts (e.g., bar graphs or pie charts) to visualize animal count distribution.

Provide trend analysis if historical data is stored.
Add a summary report displaying insights like percentage distribution of each animal.

### 2. Export and Import Data
Add the ability to export survey data to formats like CSV, Excel, or PDF.
Allow importing data from external files to update the worksheet.

### 4. Customizable Animal Categories
Let users add or remove animal categories dynamically.
Provide an interface for users to manage the categories stored in the worksheet.

### 5. Historical Data Tracking
Log all changes to the worksheet to track who made updates and when.
Include a feature to undo changes or revert to a previous state.

### 6. Survey Customization
Allow users to define their own survey questions, not just limited to animals.
Store multiple survey types within the worksheet.

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
| **Program starts** on deployed site   | User opens program  | Program begins execution on the deployed site.           | **Success** |
| **Display current data** on program open   | User opens program | Program displays current data on worksheet           | **Success** |
| **Ask user if want to reset previous data**   | User opens program | Program asks user if they want to reset previous data           | **Success** |
| **Ask if user if participants has a pet**   | After answering the first question, program ask if user if participants has a pet  | After answering the first question, program ask if user if participants has a pet           | **Success** |
| **User answer Y / N if participant has a pet**   | User answer Y / N if participant has a pet | User answer Y / N if participant has a pet. Other answers result in an error message and the question is asked again           | **Success** |
| **User answers Y if participant has a pet**   | User answers Y if participant has a pet | Program continues to next question           | **Success** |
| **User answers N if participant has a pet**   | User answers N if participant has a pet | Program ends           | **Success** |
| **Ask user what animal**   | User continues to next question | Program asks user what animal           | **Success** |
| **User answers what animal**   | User answers what animal | Program continues to next question           | **Success** |
| **User answers what animal**   | User answers an animal not in the list | Program sends error message and asks again           | **Success** |
| **Ask user if more to add**   | User continues to next question | Program asks user if more to add           | **Success** |
| **User answers Y / N if more to add**   | User answers Y / N if more to add | User answer Y / N if more to add. Other answers result in an error message and the question is asked again           | **Success** |
| **User answers Y if more to add**   | User answers Y if more to add | Program asks user what animal again          | **Success** |
| **User answers N if more to add**   | User answers N if more to add | Program ends           | **Success** |
| **End program**   | Program ends | Program updates worksheet, display summary of update values, states what highest animal count is | **Success** |


### Bugs 

### Solved
**Bug1**: While loop won’t end when answering “N” to if any more animals to add
	
    Fix: Removed the call what_animal() inside keep_asking(). Instead, what_animal() uses the return value of keep_asking() to decide whether to continue or stop.

**Bug2**: infinite loop. ask_to_reset_prev_data calls do_you_have_pets if the user chooses not to reset the data. do_you_have_pets completes and then continues back to main, which calls ask_to_reset_prev_data again.
	
    Fix: Add a return Value for ask_to_reset_prev_data (True / False), Removed do_you_have_pets() from ask_to_reset_prev_data. Streamlined main by calling ask_to_reset_prev_data once, handles the decision, and proceeds without loops.

**Bug3**: Program unable to deploy on heroku. Followed steps from instructions and put in the below code to terminal:

    pip3 freeze > requirements.txt

Did not work.
Fix: Copied requirements.txt from love-sandwiches.

    cachetools==4.2.1
    google-auth==1.27.0
    google-auth-oauthlib==0.4.2
    gspread==3.7.0
    oauthlib==3.1.0
    pyasn1==0.4.8
    pyasn1-modules==0.2.8
    requests-oauthlib==1.3.0
    rsa==4.7.2

**Bug4**: Keep getting the below message in terminal if resetting previous values. Doesn't impact funtion of the program.
Message:

    /workspaces/pet-survey-analysis-project3/run.py:126: DeprecationWarning: The order of arguments in worksheet.update() has changed. Please pass values first and range_name secondor used named arguments (range_name=, values=)
    worksheet_to_update.update('B2:B9', [[0]] * 8)
    Previous data has been reset.

Fix: Modify reset_prev_data function to use named arguments:

   	 worksheet_to_update.update(range_name='B2:B9', values=[[0]] * 8)

**Bug5**: Deployed program errors with the following message when trying to reset prev data.

    File "/app/run.py", line 223, in <module>
        main()
    File "/app/run.py", line 213, in main
        data_reset = ask_to_reset_prev_data()
                    ^^^^^^^^^^^^^^^^^^^^^^^^
    File "/app/run.py", line 115, in ask_to_reset_prev_data
        reset_prev_data()
    File "/app/run.py", line 127, in reset_prev_data
        worksheet_to_update.update(range_name='B2:B9', values=[[0]] * 8)
    File "/app/.heroku/python/lib/python3.12/site-packages/gspread/utils.py", line 587, in wrapper
        raise TypeError(err % (f.__name__, list(unexpected_kwargs)))
    TypeError: update got unexpected keyword arguments: ['values', 'range_name']

Fix: Manually updated gpsread version in requirements.txt (gspread==6.1.4 vs gspread==3.7.0).

    Ran below in terminal to get up to date version:
    pip freeze | grep gspread
    

### Remaining Bugs

None remaining

--- 


## Validator 

### PEP8 

Only errors returned were "lines too long" - Known and accepted as print statements.

![PEP8 Validation](/assets/images/petsurveyanalysis-pep8-validation.png)

--- 

## Deployment 

### Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.


### Live link:

[Pet Survey Analysis!](https://pet-survey-analysis-project3-dc2d0651f524.herokuapp.com) 


--- 

## Credits

### Outside Code
- Code Institute
    - Code terminal
    - README template
- Love sandwiches code
    - Setting up workspace 
    - Deployment
- ChatGPT code
    - Update worksheet correctly so that new additions don't create new rows/columns & each upload to worksheet doesn’t create a new line and adds onto previous result
    - getting reset prev data corrected 
    - TS'ing bug 2/4/5
- YouTube
    - Find highest number < https://www.youtube.com/watch?v=BncMTg_7H8Q > 
