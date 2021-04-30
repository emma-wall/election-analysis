import csv
import os
# Retrieve data
#Assign a variable for the file to loan and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Initialize votes variable (has to be before open because everytime we run the file it should equal 0)
total_votes = 0
candidate_options= []
#create open dictionary 
candidate_votes = {}
#declare variable that holds an empty string value for the winning candidate 
winning_candidate = ""
#delcare a varaibel for the winning count equal to zero
winning_count = 0
#delare variable for winning percentage
winning_percentage = 0

# Open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file 
    for row in file_reader:
        #print(row)
        total_votes += 1
        candidate_names = row[2]
        if candidate_names not in candidate_options:
            #Add candidate name to options
            candidate_options.append(candidate_names)
            #begin tracking candidnate vote count
            candidate_votes[candidate_names]= 0
        #add a vote to that candidate's count
        candidate_votes[candidate_names]+=1
# save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n")
    print(election_results, end = "")
    #save the final vote count to the text file
    txt_file.write(election_results)
    for candidate_names in candidate_votes:
        # get vote count of a candidate
        votes = candidate_votes[candidate_names]
        #calculate % of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #print name and % of votes      
        candidate_results = (f"{candidate_names}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if votes > winning_count and vote_percentage > winning_percentage:
            #if true, set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to candidate name
            winning_candidate = candidate_names
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    
    winning_results = winning_candidate_summary
    txt_file.write(winning_candidate_summary)
    




#print(total_votes)
#print(candidate_options)
#print(candidate_votes)

    




# Read file object with reader function


# 1. Total number of votes cast
# 2. Complete list of candidates who receive votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes candidate won
# 5. the winnder of the election based on popular vote
#Close the file