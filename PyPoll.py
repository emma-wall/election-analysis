import csv
import os
# Retrieve data
#Assign a variable for the file to loan and the path
file_to_load = os.path.join("election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)


# Read file object with reader function


# 1. Total number of votes cast
# 2. Complete list of candidates who receive votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes candidate won
# 5. the winnder of the election based on popular vote
#Close the file