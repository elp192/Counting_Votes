# Counting Votes
## Project Overview
### Background
The Input Data folder includes the .csv file ([election_results.csv](https://github.com/elp192/Election-Analysis/blob/8d9ad13ef3ed52132c0074433e553a73eedfd118/Input%20Data/election_results.csv)), which consists of data related to the Colorado Board of Elections. The .csv file consists of about 370,000 rows and 3 columns as follows:<br>
A) Ballot ID, B) Country name, C) Candidate name.
### Purpose
In this project, our aim is to develop a code that helps us determine the total number of votes, percentage of votes for each candidate and country, a country with the highest voter turnout, a winner candidate, etc. The output results are saved to [election_analysis.txt](https://github.com/elp192/Election-Analysis/blob/8d9ad13ef3ed52132c0074433e553a73eedfd118/Output%20Data/Election%20Analysis.txt) file.<br>
Python (version 3.8.8) is used as the coding language, and the code is written in Visual Studio Code. The code written to analyze this data can be utilized to count the votes related to other election datasets.
## Explanations about code 
The important steps to create the code and analyze the election results are as follows:<br>
1) Loading a file from a specific path and saving the file to a specific path using os.path.join() method:

       file_to_load=os.path.join("Input Data","election_results.csv")
       file_to_save=os.path.join("analysis","election_analysis.txt")
2) Initializing the counter, list, and dictionary related to candidate and country.
3) Opening and reading the .csv file:
 
       with open(file_to_load) as election_data:
       reader = csv.reader(election_data)
4) Defining For Loop to iterate through each row of .csv file: <br>
   - Calculated total votes and determine candidate name (column 3) and country name (column 2) in each row: 
       
         for row in reader:
           total_votes = total_votes + 1
           candidate_name = row[2]
           country_name = row[1]
   - Creating a list of country and candidate, and counted country and candidate votes in dictionary using if condition:
     
          if candidate_name not in 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
          candidate_votes[candidate_name] += 1
         
          if country_name not in country_list:
            country_list.append(country_name)
            country_votes[country_name] = 0
          country_votes[country_name] += 1
            
 5) Saving and writing the results:

         with open(file_to_save, "w") as txt_file:
         txt_file.write(election_results)
 6) Defining For Loop to get country votes from dictionary and calculate percentage of votes for the country:
 
        for country in country_votes:
            country_vote=country_votes.get(country)
            country_vote_percentage = float(country_vote) / float(total_votes) * 100
    - Saving and writing the results to text file:
    
            txt_file.write(country_results)
    - Determining the winning country using if condition:
            
            if (country_vote > country_count):
            country_count = country_vote
            country_largest = country
            country_percentage = country_vote_percentage  
 7) Defining For Loop to get candidate votes from dictionary and calculate percentage of votes for the each candidate:
           
        for candidate_name in candidate_votes:
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100 
            txt_file.write(candidate_results)
     - Saving and writing the results to text file:
     
            txt_file.write(candidate_results)
     - Determining the winning candidate using if condition:
     
            if (votes > winning_count) and (vote_percentage > winning_percentage):
               winning_count = votes
               winning_candidate = candidate_name
               winning_percentage = vote_percentage
## Results
In this section, the election results are reported based on countries (i.e., Jefferson, Denver, Arapahoe) and candidates (i.e., Stockham, DeGette, and Doane).<br>
- Countries Outcomes:<br>
  - The total number of votes is 369,711 in this congressional election.<br>
  - Jefferson had 10.5% of the votes (38.855 votes).<br>
  - Denver had 82.8% of the votes (306,055 votes).<br>
  - Arapahoe had 6.7% of the votes (24,801 votes).<br>
:white_check_mark: Among the countries, the highest vote is allocated to Denver by about 83% (306,055 votes). However, The percentage of votes for Jefferson and Arapahoe is the lowest at 10.5% (38,855 votes) and 6.7% (24,801 votes), respectively (see Figure 1, left). <br>
- Candidates Outcomes:<br>
  - Charles Casper Stockham received 23% of the votes (85,213 votes out of 369,711 votes).<br>
  - Diana DeGette received 73.8% of the votes (272,892 votes out of 369,711 votes).<br>
  - Raymon Anthony Doane received 23% of the votes (85,213 votes out of 369,711 votes)<br>
:white_check_mark: The winner of this election is Diana DeGette, with 73.8% of the votes (272,892 votes)(see Figure 1, right).<br>

<p img align="center" width="100%">
   <img width="236" alt="Country_Results" src="https://user-images.githubusercontent.com/85843401/125961645-d941a20e-ef57-4af1-80b7-54d4495f32d9.png">
   <img width="288" alt="Candidate_Results" src="https://user-images.githubusercontent.com/85843401/125962178-bcd2f823-e797-4c6a-9876-f0adfe23558e.png"><figcaption>Figure 1: Demonstration of election results. Left) Country, Right) Candidate .</figcaption></figure/> 
<p align="center">
</p>

## Summary
This python code can be reused to calculate the outcomes of other types of election even with larger datasets. However, minor modifications need to be applied. The examples of these modifications are as follows:<br>
:white_small_square: The line that the variable is added to load a file from a path should be substituted by a new file. If an input file is not a .csv file, related dependency will be imported.<br>
:white_small_square: The lines that depend on the structure of the loaded file (i.e.,```county_name = row[1]``` and ```candidate_name = row[2]```) need to be modified. For example, in our input file, the ballot ID, country name, and candidate name are the heaters of columns 1-3, respectively. In a new file with a different structure, these lines that call columns should be modified accordingly.
 

