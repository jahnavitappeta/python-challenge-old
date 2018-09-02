import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    voter_count = 0
    candidates = {}


    for row in csvreader:
        voter_count += 1
        candidates[row[2]] = candidates.get(row[2], 0) + 1


    fileContent = str(f'Total votes {voter_count}\n')
    for k,v in candidates.items():
        percent_voter = v/voter_count * 100
        fileContent += str(f'{k}: {round(percent_voter, 2)}% ({v})\n')

    winner = max(candidates,key=candidates.get)
    fileContent += str(f'Winner: {winner}')

    print(fileContent)
    file = open('Output.txt','w')
    file.write(fileContent)
    file.close()

