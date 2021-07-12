import csv
import os
#Assign variable to load
file_to_load=os.path.join("Input Data","election_results.csv")
#Assign variable to save output
file_to_save=os.path.join("analysis","election analysis.txt")
#print(file_to_save)
#open input and read
Candidate_List=[]
Candidate_Votes={}
#open and read file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     headers=next(file_reader)
     #print(headers)
     
     Total_votes=0
     for row in file_reader:   
#calculate total votes 
         Total_votes+=1
         if row[2] not in Candidate_List:
#Add each candidate to the list
           Candidate_List.append(row[2])
           Candidate_Votes[row[2]]=0
#Calculate votes for each candidate
         Candidate_Votes[row[2]]+=1

     Percentage_votes=[]
     Winning_number=0
     Winning_percentage=0
     for candidate in Candidate_List:
         Each_votes=Candidate_Votes[candidate]
         #calculate percentage of votes for each candidate
         Percentage=(float(Each_votes)/float(Total_votes))*100
         #Percentage_votes.append(Percentage)
         #print(f"{candidate}, received {Percentage}% of the vote") 
         #determine winner candidate
         if (Each_votes> Winning_number) and (Percentage > Winning_percentage):
             Winner_number=Each_votes
             Winner_percentage=Percentage
             Winner_name=candidate
     print(f"{candidate}:{Percentage:.1f}%({Each_votes:,})")
     #print(f"{Winner_name} was the winner of the election with {Winner_percentage} ofthe vote and {Winner_number} votes.")
     winner_candidate = (
     f"-------------------------\n"
     f"Winner: {Winner_name}\n"
     f"Winning Vote Count: {Winner_number:,}\n"
     f"Winning Percentage: {Winner_percentage:.1f}%\n"
     f"-------------------------\n")
     print(winner_candidate )

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
