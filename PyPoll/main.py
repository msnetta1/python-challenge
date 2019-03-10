import os
import csv

csvpath =  'election_data.csv'

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv header  = next(csvreader)

    total_votes = 0
    candidates ={}

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        total_votes = total_votes + 1

        if candidate in cadidates:
            candidates[candidate] + 1
        else:
            candidates[candidate] = 1

highest_number_of_votes = 0
winner = None          

print('Election Results')
print('Total Votes: &d'%total_votes)
for candidate, votes in candidates.items():
    perecentage = votes / total_votes * 100
    print('%s: %.2f%% (%d)'%candidate, percentage, votes))
    if votes > highest_number_of_votes:
        winner = candidate
        highest_number_of_votes = votes

print('Winner: %s'winner)


