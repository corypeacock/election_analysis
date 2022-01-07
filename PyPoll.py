# Overview
## 1. The data we need to retrieve
## 2. A complete list of candidates who received votes
## 3. The percentage of votes each candidate won
## 4. The total number of votes each candidate won
## 5. The winner of the election based on popular vote.

# import dependencies
import csv

# variables for opening data and saving analysis to files
file_to_load = 'resources/election_results.csv'
file_to_save = 'analysis/election_analysis.txt'

# open the election results and read file
with open(file_to_load) as election_data:

    # read and analyze the data here
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)

# # open file and write analysis
# with open(file_to_save, 'w') as txt_file:

#     # write some data to the file
#     txt_file.write('Counties in the Election\n')
#     txt_file.write('-'*24 + '\nArapahoe\nDenver\nJefferson')
