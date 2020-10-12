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
    print(csv_header)
    for row in ElectionData:
        votes = votes + 1
        if row[2] not in candidates:
           candidates[row[2]] = 1

        else:
            candidates[row[2]] += 1
    for candidate in candidates:
        cand_per = (candidates[candidate]/votes)*100
        print(cand_per)


print(candidates)
print(votes)
