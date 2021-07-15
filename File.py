# Add dependencies.
import csv
import os

#Assign variable to load file
file_to_load=os.path.join("Input Data","election_results.csv")
#Assign variable to save output
file_to_save=os.path.join("Output Data","Election Analysis.txt")

# Initialization
total_votes = 0

candidate = []
candidate_votes = {}

country_list=[]
country_votes={}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

country_largest=""
country_count=0
country_percentage = 0

# Read the csv and convert it into a list of dictionaries.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        #select candidate name and country in each row.
        candidate_name = row[2]
        country_name = row[1]

        if candidate_name not in candidate:
            #add the candidate to the list.
            candidate.append(candidate_name)
            #initialize the value of dictionary.
            candidate_votes[candidate_name] = 0
            #count the votes related to specific candidate.
        candidate_votes[candidate_name] += 1

        if country_name not in country_list:
            #add the country to the list.
            country_list.append(country_name)
            #initialize the value of dictionary.
            country_votes[country_name] = 0
            #count the votes related to specific candidate.
        country_votes[country_name] += 1

# Save the results to text file.
with open(file_to_save, "w") as txt_file:

    # Print 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    
    for country in country_votes:
        #get the count of vote for country.
         country_vote=country_votes.get(country)
        # votes percentage for the county.
         country_vote_percentage = float(country_vote) / float(total_votes) * 100
         #print
         country_results = (
             f"{country}: {country_vote_percentage:.1f}% ({country_vote:,})\n")
         print(country_results)
         #Save the county votes to a text file.
         txt_file.write(country_results)

         #Determine the winning county and get its vote count.
         if (country_vote > country_count):
            country_count = country_vote
            country_largest = country
            country_percentage = country_vote_percentage  

    # Print 
    country_largest_turnout_summary = (
            f"-------------------------\n"
            f"Largest Country Turnout: {country_largest}\n"
            f"-------------------------\n")
    print(country_largest_turnout_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(country_largest_turnout_summary)

    for candidate_name in candidate_votes:
         #get the count of vote for candidate
        votes = candidate_votes.get(candidate_name)
        # votes percentage for the candidate.
        vote_percentage = float(votes) / float(total_votes) * 100
        #print
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to the text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, candidate, and winning percentage.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save to the text file.
    txt_file.write(winning_candidate_summary)
