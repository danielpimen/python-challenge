import os
import csv
#The total number of votes cast
election_csv = os.path.join("election_data.csv")
file = open(election_csv)
numline = len(file.readlines())
print ("The total number of votes is" , int(numline - 1))

#A complete list of candidates who received votes
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0 
total_votes = 0

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    for row in csvreader:
        
        #calculate total votes
        total_votes += 1
        #The total number of votes each candidate won
        #calculate number of votes for each of the candidates
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
    print("Khan got" , khan_votes, "Votes" )
    print("Correy got" ,correy_votes, "Votes")
    print("Li got" ,li_votes, "Votes")
    print("Otooley got" ,otooley_votes, "Votes")

#The percentage of votes each candidate won
percent_khan = khan_votes / total_votes
print(percent_khan)
percent_correy = correy_votes / total_votes
print(percent_correy)
percent_li = li_votes / total_votes
print(percent_li)
percent_otooley = otooley_votes / total_votes
print(percent_otooley)

#The winner of the election based on popular vote.
winner = max(khan_votes, correy_votes, otooley_votes, li_votes)
print("The Winner got" , winner, "Votes")