#! python

# Overview
## 1. The data we need to retrieve
## 2. A complete list of candidates who received votes
## 3. The percentage of votes each candidate won
## 4. The total number of votes each candidate won
## 5. The winner of the election based on popular vote.

# import dependencies
import csv
import os

# variables for opening data and saving analysis to files
file_to_load = 'resources/election_results.csv'
file_to_save = 'analysis/election_analysis.txt'

# initialize total vote counter
total_votes = 0

# init candidate list & dictionary for votes per candidate
candidate_options = []
candidate_votes = {}

# winning candidate, vote, and percentage trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election results and read file
with open(file_to_load) as election_data:

    # read and analyze the data here
    file_reader = csv.reader(election_data)

    # read the header row - and to move on to the rows with data
    headers = next(file_reader)

    # print each row
    for row in file_reader:
        # increment total vote count
        total_votes += 1

        #print the candidate name for each row
        candidate_name = row[2]

        # add candidate name to candidate list if name already not in options list
        if candidate_name not in candidate_options:
            # add name to the list of candidates
            candidate_options.append(candidate_name)
            # beging tracking new candidate's vote count
            candidate_votes[candidate_name] = 0

        # increment vote count if candidate is already in the candidate options list
        candidate_votes[candidate_name] +=1

# open file to save to and write analysis
with open(file_to_save, 'w') as txt_file:

    # print final vote count to terminal
    election_results = (
    f'\nElection Results\n'
    f'------------------------------\n'
    f'Total Votes: {total_votes:,}\n'
    f'------------------------------\n')

    print(election_results, end="")

    # save the final vote count to the text file
    txt_file.write(election_results)

    # determine each candidates percentage of vote won
    for candidate_name in candidate_votes:
        # retrieve vote count & percentage for candidate
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # capture result of each candidate
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        # print each candidates info to terminal
        print(candidate_results)
        # save the candidate results to our text file
        txt_file.write(candidate_results)

        # determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set winning_candidate equal to candidate's name
            winning_candidate = candidate_name

    # winning candidate
    winning_candidate_summary = (
        f'-'*30 + '\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'------------------------------\n')

    # print(winning_candidate_summary)
    print(winning_candidate_summary)

    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
