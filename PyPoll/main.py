#!/usr/bin/env python
# coding: utf-8

# 
# #In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process

# In[14]:


#Set up import and export files for data and analysis results


# In[15]:


#Import Dependencies
import csv
import os


# In[16]:


#Make a reference to the election_data.csv
file_to_load = os.path.join("PyPoll","Resources","election_data.csv")
file_to_load


# In[17]:


#Make a reference to the export file
file_to_save = os.path.join("PyPoll","Analysis","pypoll_analysis.txt")
file_to_save


# Election Data Analysis

# In[18]:


# Set the variables
total_votes = 0
candidates = {}


# In[19]:


#Open and read the CSV file
with open(file_to_load, mode='r') as election_data:
    csv_reader=csv.DictReader(election_data)

    # Process each row in the csv
    for row in csv_reader:
        total_votes += 1
        candidate = row['Candidate']

        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] = 1


# In[20]:


# Calculate the percentage of total votes, announce a winner and store results in a list for each candidate
winner = ""
max_votes = 0
candidate_results = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes)*100
    candidate_results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > max_votes:
        max_votes = votes
        winner = candidate


# In[21]:


#store election results in a variable to call and print

election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"  
    f"{candidate_results[0]}\n"
    f"{candidate_results[1]}\n"
    f"{candidate_results[2]}\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n")
    
print(election_results)


# In[10]:


# Write the results to a text file
with open(file_to_save, mode='w') as file:
    file.write(election_results)


# In[ ]:




