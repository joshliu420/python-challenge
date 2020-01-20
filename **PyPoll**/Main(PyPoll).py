import os
import csv
from collections import Counter


# open the file
PyPoll_path = os.path.join('Resources', 'election_data.csv')

with open(PyPoll_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # create a list for column "Candidate" for furthur calculation
    vote_list = [row[2] for row in csvreader]

    # count the frequency for each name
    vote_dic = Counter(vote_list)
    # extract candidate's name and the votes they got
    name_list = [name for name in vote_dic.keys()]
    vote_count = [vote for vote in vote_dic.values()]

    # calculate total votes
    total_votes = sum(vote_count)
    
    # calculate the percentage for each candidate got
    pct_list = []
    for i in range(len(vote_count)):
        percentage = "{0:.3%}".format(float(vote_count[i]) / float(total_votes))
        pct_list.append(percentage)

    # locate the winner name
    winner = name_list[vote_count.index(max(vote_count))]

    # print out the result
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    for i in range(len(name_list)):
        print(f'{name_list[i]}: {pct_list[i]} ({vote_count[i]})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
    
    # set up the output path and prepare to export the result
    output_path = os.path.join("PyPoll_output.txt")
    with open(output_path, 'w', newline='') as txtoutput:

        # Initialize csv.writer
        txtwriter = csv.writer(txtoutput, delimiter=',')

        # Write row by row
        txtwriter.writerow(['Election Results'])
        txtwriter.writerow(['-------------------------'])
        txtwriter.writerow(['Total Votes', str(total_votes)])
        txtwriter.writerow(['-------------------------'])
        for i in range(len(name_list)):
            txtwriter.writerow([name_list[i], pct_list[i], vote_count[i]])
        txtwriter.writerow(['-------------------------'])