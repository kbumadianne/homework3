#!/usr/bin/env python
# coding: utf-8

# #Create a Python script to analyze the finanical records of your company

# Set up import and export files for data and analysis results

# In[68]:


#Import Dependencies
import csv
import os


# In[69]:


#Make a reference to the budget_data.csv
file_to_load = os.path.join("PyBank/Resources/budget_data.csv")
file_to_load


# In[70]:


#Make a reference to the export file
file_to_output = os.path.join("PyBank/Analysis/pybank_analysis.txt")
file_to_output


# Financial Analysis

# In[74]:


# Initialize variables
total_months = 0
total_net = 0
change_list = []
prev_net = None
greatest_increase = ["", float('-inf')]
greatest_decrease = ["", float('inf')]

# Open CSV file
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    # Skip the header
    header = next(reader)

    # Process the first row
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process subsequent rows
    for row in reader:
        total_months += 1
        current_net = int(row[1])
        total_net += current_net

        # Calculate change
        net_change = current_net - prev_net
        change_list.append(net_change)
        prev_net = current_net

        # Check for greatest increase and decrease
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate average change
average_change = sum(change_list) / len(change_list) if change_list else 0


# In[81]:


# Format the output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



# In[83]:


# Print and save the results
print(output)
with open(file_to_output, 'w') as text_file:
    text_file.write(output)


# In[ ]:




