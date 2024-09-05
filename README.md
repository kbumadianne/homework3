# homework3
python-challenge

PyBank Challenge code explanation:
First I needed to import dependencies from panda and pathlib to import the csv data file and turn that data file into a Dataframe
After checking the data imported correctly and using the encoding that matched the csv file I was able to proceed with financial analysis
In order to track the data within different calculations and more easily print the data I created variables for each of the requests prior to using formulas to find the needed data
Total number of months included in the dataset - I was able to use a count function on the Date series to execute this task.  I had to turn the chosen stored variable "Months" into a string and integer to be able to concatenate in the print function
The net total amount of "Profit/Losses" over the entire period - I created another variable to store the Sum of the Profit/Losses series and printed in a similar code to the above line
The changes in "Profit/Losses" over the entire period, and then the average of those changes - I needed to add a new column to the dataframe and add a calculation to the variable stored in the column to be able to see the profit and losses over the entire period
The calculation to see the total profit and losses uses the "diff" function from the panda import on the Dataframe.  This function calculates the difference from the previous row in a data series.  This allowed me to track the change over the entire period
Using the mean function I was able to calculate the average of the profit loss change and store this to a new variable. To print this variable I had to use a f string because the average had decible points and I needed to show that as a float, not integer
I used a similar thought process with max increase and max decrease of the profit loss change.  I used the min and max function on the profit loss change series to be able to store those values to a variable.
For the dates tied to the max increase and decrease, I used the idxmax and idxmin functions combined with loc to find the index that corresponds to the min and max values of the profit loss change.
