import os
import csv
votes = 0


electiondatapath = "Resources/election_data.csv" # point to Election data csv file
# create null dictionary to store candidate names
candidates = {}
#Open ElectionData.csv
with open(electiondatapath) as csvfile:
    ElectionData = csv.reader(csvfile, delimiter=',')
    csv_header = next(ElectionData)

    for row in ElectionData:
        votes = votes + 1
        if row[2] not in candidates:
           candidates[row[2]] = 1

        else:
            candidates[row[2]] += 1
    name = ""
    win_count = 0        
    for candidate in candidates:
        cand_per = (candidates[candidate]/votes)*100

        #If statement candidate with most votes wins. Store greatest votes
        
        if candidates[candidate] > win_count:
            win_count = candidates[candidate]
            name = candidate

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
winner_votes = 0
winner_candidate = ""
for candidate in candidates:
    print(f"{candidate}: {(candidates[candidate]/votes)*100:.3f}% ({candidates[candidate]})")
    if candidates[candidate] > winner_votes:
        winner_votes = candidates[candidate]
        winner_candidate = candidate
print("-------------------------")
print(f"Winner:{name}")
print("-------------------------")

