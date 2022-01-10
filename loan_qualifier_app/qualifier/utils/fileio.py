# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
import sys

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
      
    # Ask user if they would like to save the file?
    save_ask = questionary.text("Would you like to save the qualifying loan data to a csv file? Yes or No").ask()

    # Based on user input, yes or no, a if condition excutes as a filter.
    if save_ask == "Yes" or save_ask == "yes":
        save_ask = True
        
        #User asked for file path as a save folder. Then the user is asked for a file name. *** File name only. Example: Qualifing_Loans
        save_path = questionary.text("Please specify the entire folder path to save this file:").ask()
        save_file_name = questionary.text("What would you like the file name to be? as a (.csv)").ask()

        #File name and path converted into a .csv file path.
        save_path = save_path + f"\{save_file_name}"

        #Headers added to the csv file.
        headers = ["Lender","Max Loan","Amount","Max LTV","Max DTI","Min Credit Score","Interest_Rate"]

        #csv writer is used from the csv library.
        #print(qualifying_loans)
        with open(save_path, 'w', newline='') as file:
            writer = csv.writer(file)
            #Headers and qualifying_loans list of list are written to the csv file.
            writer.writerow(headers)
            writer.writerows(qualifying_loans)

            #Message sent to user of successful save
        sys.exit(f"File saved successfully as {save_file_name} file. - Good Bye!")

    #Conditions for if the user answers No.
    elif save_ask == "No" or save_ask == "no":
        save_ask = False
        sys.exit("File was not saved.")

    #Condition for any other input.
    else:
        sys.exit("You did not answer Yes or No - Exiting System.")    
