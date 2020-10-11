# The data we need to retrieve.
#1. The total number of votes to cast 
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

#Add our dependencies. 
import csv
import os

#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("/Users/Mac_1/Desktop/Analysis_Projects/Election_Analysis/Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/Mac_1/Desktop/Analysis_Projects/Election_Analysis/Resources/analysis", "election_analysis.txt")

#1. Initialize a total vote counter. 
total_votes = 0
#declaring a new list for candidates
candidate_options = []
#3.5.3-1 Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open (file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    #read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #3.5.3-2 Begin tracking that candidates's vote count.
            candidate_votes[candidate_name] = 0

        #3.5.3-3 Add a vote to that candidates's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end=" ")
    #save the final vote count to the text file.
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100 
        #To do: print out each candidate's name, vote count, and percentage of 
        # votes to the terminal 
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #print each candidate, their voter count, and percentage to the terminal. 
        print(candidate_results)
        #save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count. 

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning count_count = votes and winning_perfectage = 
            #vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    #print out the winning candidate, vote count and percentage to 
    #terminal 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"--------------------------\n")
    #print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

