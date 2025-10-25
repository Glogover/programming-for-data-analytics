# assignment02-bankholidays.py
# This program prints the bank holidays that are unique to Northern Ireland

# Author: Marcin Kaminski

import requests  # Import the requests module to handle HTTP requests
import json # Import the JSON module to work with JSON data

FILENAME = 'ukbankholidays.json' # Define the filename containing the JSON data
URL = "https://www.gov.uk/bank-holidays.json" # Define the URL to fetch the JSON data from

# with open(FILENAME, 'rt') as file: # Open the JSON file for reading
    # data = json.load(file)  # Load JSON data from the file and converts it into a Python dictionary

# Fetch JSON data from the UK government website
response = requests.get(URL) # Send a GET request to the specified URL
data = response.json() # Parse the JSON response into a Python dictionary  

# Save a local copy of the JSON data
with open(FILENAME, 'wt') as file: # Open the file for writing
    json.dump(data, file, indent = 2)  # Write the JSON data to the file with indentation for readability
print(f"Local copy of JSON data saved to {FILENAME}") # Print a confirmation message

# Collect Northern Ireland bank holidays
NI_holidays = [] # Initialize an empty list to store Northern Ireland bank holidays
for holiday in data['northern-ireland']['events']: # Loop through each holiday in Northern Ireland
    NI_holidays.append({"title": holiday['title'], "date": holiday['date']}) # Append the title and date of each holiday to the list

# Collect all other UK regions bank holiday titles
other_titles = [] # Initialize an empty list to store titles of bank holidays from other UK regions
 

print("Bank holidays in Northern Ireland:") # Print a header message
for holiday in data['northern-ireland']['events']: # Loop through each holiday
    print(f"{holiday['date']}: {holiday['title']}") # Print the date and title of each holiday
      
