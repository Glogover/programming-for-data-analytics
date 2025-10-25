# This program prints out the dates of the bank holidays that happen in Northern Ireland.
# Author: Marcin Kaminski

import json # Import the JSON module to work with JSON data

FILENAME = 'ukbankholidays.json' # Define the filename containing the JSON data

with open(FILENAME, 'rt') as file: # Open the JSON file for reading
    data = json.load(file)  # Load JSON data from the file and converts it into a Python dictionary
    print("Bank holidays in Northern Ireland:") # Print a header message
    for holiday in data['northern-ireland']['events']: # Loop through each holiday
        print(f"{holiday['date']}: {holiday['title']}") # Print the date and title of each holiday
      
