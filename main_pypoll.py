import os
import csv
import statistics
election_csvpath = os.path.join('..','Resources','election_data.csv')
election_output = os.path.join('..','Resources','pypoll_results')
candidates=['Khan', 'Correy', 'Li', 'OTooley']

# Initialize values 
Total_votes = 0
candidates=[]
Correy_votes=0
Khan_votes=0
OTooley_votes=0
Li_votes=0

with open(election_csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        for row in csvreader:
            Total_votes += 1
            if row[2] not in candidates:
                candidates.append(row[2])
            if row[2]==candidates[0]:
                Khan_votes +=1
            elif row[2]==candidates[1]:
                Correy_votes +=1
            elif row[2]==candidates[2]:
                Li_votes +=1
            elif row[2]==candidates[3]:
                OTooley_votes +=1

def percent(votes):
        percent=round(((votes/Total_votes)*100),2)
        return(percent)

Khan_percent=percent(Khan_votes)
Correy_percent=percent(Correy_votes)
Li_percent=percent(Li_votes)
OTooley_percent=percent(OTooley_votes)

Khan=(candidates[0],Khan_percent, Khan_votes)
Correy=(candidates[1], Correy_percent, Correy_votes)
Li=(candidates[2], Li_percent, Li_votes)
OTooley=(candidates[3], OTooley_percent,OTooley_votes)

candidate_list=(Khan, Correy, Li, OTooley)
winner=max(candidate_list, key = lambda kv : kv[1])
# print_content="Election Results"
# print_content("Election Results")
# print('.............................')
print(f'Total Votes: ({Total_votes})')
# print('.............................')
print(f'{candidates[0]}: {Khan_percent}% ({Khan_votes})')

print(f'{candidates[1]}: {Correy_percent}% ({Correy_votes})')

print(f'{candidates[2]}: {Li_percent}% ({Li_votes})')

print(f'{candidates[3]}: {OTooley_percent}% ({OTooley_votes})')

print(f'Winner: {winner[0]}')


print_content = (f"FinanciaElection Results\n"
                 f"------------------------\n"
                 f"Total Votes: {Total_votes}\n"
                 f"Khan Results: {Khan_votes} ({Khan_percent}%)\n"
                 f"Correy Results: {Correy_votes} ({Correy_percent}%)\n"
                 f"Li Results: {Li_votes} ({Li_percent}%)\n"
                 f"OTooley Results: {OTooley_votes} ({OTooley_percent}%)\n"
                 f"Winner is: {winner[0]}\n")                          
with open(election_output, "w") as text_file:
        text_file.write(print_content)       