import csv
import os
#Assign variable to load
file_to_load=os.path.join("Input Data","election_results.csv")
#Assign variable to save output
file_to_save=os.path.join("analysis","election analysis.txt")
#print(file_to_save)
Candidate_list=[]
Candidate_votes={}
#open and read file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     headers=next(file_reader)
     #print(headers)
     
     Total_votes=0
     for row in file_reader:   
#calculate total votes 
         Total_votes+=1
         if row[2] not in Candidate_list:
#Add each candidate to the list
           Candidate_list.append(row[2])
           Candidate_votes[row[2]]=0
#Calculate votes for each candidate
         Candidate_votes[row[2]]+=1
         # Save Results to text file.
         
     with open(file_to_save, "w") as txt_file:

        election_results=(
            f"Election Results\n"
            f"----------------\n"
            f"Total Votes: {Total_votes:,}\n"
            f"----------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
            
        Percentage_votes=[]
        Winner_name=""
        Winner_number=0
        Winner_percentage=0
        for candidate in Candidate_list:
            Each_votes=Candidate_votes[candidate]
            #calculate percentage of votes for each candidate
            Percentage=(float(Each_votes)/float(Total_votes))*100
            #Percentage_votes.append(Percentage)
            #print(f"{candidate}, received {Percentage}% of the vote") 
            #determine winner candidate
            Election_results=(f"{candidate}:{Percentage:.1f}%({Each_votes:,})\n")
            print(Election_results)
            txt_file.write(Election_results)
            if (Each_votes> Winner_number) and (Percentage > Winner_percentage):
                Winner_number=Each_votes
                
                Winner_percentage=Percentage
                Winner_name=candidate
    
        #print(f"{Winner_name} was the winner of the election with {Winner_percentage} ofthe vote and {Winner_number} votes.")
        Winner_candidate = (
            f"-------------------------\n"
            f"Winner: {Winner_name}\n"
            f"Winning Vote Count: {Winner_number:,}\n"
            f"Winning Percentage: {Winner_percentage:.1f}%\n"
            f"-------------------------\n")
        print(Winner_candidate )
        txt_file.write(Winner_candidate)
##Option 2
# #Determine the winner
# #Comparison=Candidate_Votes.values
# #Comparison=next(iter(Candidate_Votes))
# Comparison=list(Candidate_Votes.values())[0]
# for key, value in Candidate_Votes.items():
#     if value>Comparison:
#         Winner_value=value
#         Winner_name=key
#         Winner_percentage_votes=(float(Winner_value)/float(Total_votes))*100
# print(f"{Winner_name} was the winner of the election with {Winner_percentage_votes} ofthe vote and {Winner_value} votes.")    