#Psuedocode (fake code list)
# THE DATA WE NEED TO RETRIEVE
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the Election based on popular vote
#*** PATH to election_results.csv: Resources\election_results.csv
## *OPTION 2(if its not in the resouces folder but on the same level as PyPoll)
#OPTION 2: election_results.csv

#** Import csv and os modules
import csv
import os

#***ASSIGN A VARIABLE FOR THE FILE TO LOAD AND THE PATH.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with  open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
#for row in file_reader:
        #print(row)


# To do: perform analysis.
    #print(election_data)

# close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file. Adding the comma spaces them
     txt_file.write("Arapahoe\nDenvern\nJefferson ")
#CLOSE THE FILE
txt_file.close()
