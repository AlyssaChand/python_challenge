#poll

import os
import csv

poll_csv= os.path.join("resources", "election_data.csv")
#"C:\Users\alyss\OneDrive\Desktop\Python\python_challenge\pypoll\resources\election_data.csv"

#list that stores data
vote= []
candidate= []
#name_dict= {}


#variables set to 0
totalvote= 0
CharlesCasperStockham= 0
DianaDeGette= 0
RaymonAnthonyDoane= 0

with open(poll_csv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    header= next(csvreader)

    for row in csvreader:

        vote.append(int(row[0]))
        candidate.append(row[2])

        #total number of votes 
        totalvote += 1

        #candidates and their votes
        name = row[2]
        if name == "Charles Casper Stockham":
            CharlesCasperStockham += 1
        elif name == "Diana DeGette":
            DianaDeGette += 1
        elif name == "Raymon Anthony Doane":
            RaymonAnthonyDoane += 1

        #percentage of votes for each candidate
        percentcharles= round((CharlesCasperStockham/totalvote)*100,3)
        percentdiana= round((DianaDeGette/totalvote)*100,3)
        percentraymon= round((RaymonAnthonyDoane/totalvote)*100,3)

        #winner of election based on popular vote
        candidates= [CharlesCasperStockham, DianaDeGette, RaymonAnthonyDoane]
        winner= max(candidates)
        

#print results
print("                    ")
print("Election Results")
print("                    ")
print("--------------------")
print("                    ")
print(f"Total Votes: {totalvote}")
print("                    ")
print("--------------------")
print("                    ")
print(f"Charles Casper Stockham: {percentcharles}% ({CharlesCasperStockham})")
print(f"Diana DeGette: {percentdiana}% ({DianaDeGette})")
print(f"Raymon Anthony Doane: {percentraymon}% ({RaymonAnthonyDoane})")
print("                      ")
print("----------------------")
print("                      ")
print(f"Winner: {winner}")
print("                      ")
print("----------------------")
