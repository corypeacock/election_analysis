# election_analysis
Mod 3 Election Analysis using Python, (fake data)

## Project Overview
The Colorado Board of Elections requested an election audit of a recent local congressional election. The following report analyzes the election results of a congressional district in Colorado comprising Arapahoe, Denver, and Jefferson counties. This analysis will help to certify the election results for this county.  

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.63.2

## Election Audit Results
The following election outcomes should be noted.  
* 369,711 total votes were cast in this district.  
* Each county accounted for the following vote counts and percentages:  
	* Jefferson: 10.5% (38,855)  
	* Denver: 73.8% (272,892)  
	* Arapahoe: 6.7% (24,801)  
* Denver county accounted for the most votes (306,055).  
* Each candidate received the following vote counts and percentages:  
	* Charles Casper Stockham: 23.0% (85,213)  
	* Diana DeGette: 73.8% (272,892)  
	* Raymon Anthony Doane: 3.1% (11,606)  
* Diana DeGette won the election with 73.8% of the vote, receiving 272,892 votes.  

Below is the official output from the Python script for verification

![Imgur](https://i.imgur.com/dISWszQ.png)

## Election Audit Summary
Using a Python script, this analysis was generated from a csv file containing every vote cast. The output of the code included a terminal generated preview of the election results and a text file with the same results.  

### Script Advantages
A major advantage to this automation is that the script can be utilized with other voting districts. The code itself generates the report from the information in the csv file, utilizing no user input. This reduces the potential for user error when gathering candidate and county names, vote counts, and percentages. Here is a small example of the information gathering process from the Python code.

~~~
# If the candidate does not match any existing candidate add it to
# the candidate list
if candidate_name not in candidate_options:

    # Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)

    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0
~~~

This code determines whether a candidate's name has been added to the list of tracked candidates for a given election. If the candidate's name is not already in the list of tracked candidates, the name will be added to the list and a vote count will be initialized at zero votes. Another section of the code increments the vote by 1 for every vote cast for a candidate.  

After the script determines the number of votes received and the percentage of votes received for every candidate and county, the winner is determined by noting the highest vote count by candidate or county and provides that information in the terminal screen and text file. The follow code is an example of this evaluation.  
~~~  
for county_name in county_votes:
    # 6b: Retrieve the county vote count.
    covotes = county_votes.get(county_name)

    # 6c: Calculate the percentage of votes for the county.
    covote_percentage = float(covotes) / float(total_votes) * 100        

    # 6d: Print the county results to the terminal.
    county_results = (f'{county_name}: {covote_percentage:.1f}% ({covotes:,})\n')
    print(county_results, end='')

    # 6e: Save the county votes to a text file.
    txt_file.write(county_results)

    # 6f: Write an if statement to determine the winning county and get its vote count.
    if (covotes > winning_co_count):
        winning_co_count = covotes
        winning_county = county_name

# 7: Print the county with the largest turnout to the terminal.
winning_county_summary = (
    f'\n-------------------------\n'
    f'Largest County Turnout: {winning_county}\n'
    f'\n-------------------------\n')
    
print(winning_county_summary)

# 8: Save the county with the largest turnout to a text file.
txt_file.write(winning_county_summary)
~~~  

### Potential Script Improvements
This script is only useful where two variables are being tracked. In this case, the script tracks candidates and counties. A first opportunity for improvement includes the variables tracked. The script could be refactored to track further variables as needed. Examples could include more vote-specific data, such as polling location or method of vote cast. Additionally, the script could potentially be refactored to require user input to determine which variables should be tracked and how they should be named.  

A second opportunity for improvement would be for the script to handle multple elections in a single voting district. This could potential reduce the need for multiple csv files for every election within a district, requiring only one.
