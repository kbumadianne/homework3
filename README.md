# homework3
python-challenge
Analysis folders contain txt files.
PyBank folder main.py is the python code PyBank
PyPoll folder main.py is the python code for PyPoll

Printing in terminal may give an error due to the "file_to_load" path.  This worked fine in VS and Jupyter Notebook scripts, however in Git Bash it needs "PyPoll" removed in the line of code (See Below)
PyPoll file main.py code in line 25 file_to_load = os.path.join("PyPoll","Resources","election_data.csv")
Only solve I could find was providing the absolute path, which was going to error out the code when anyone else ran it, please let me know if there's another solution.  This was the file hierarchy that was outlined in the requirements.

Printing in terminal may give an error due to the "file_to_load" path.  This worked fine in VS and Jupyter Notebook scripts, however in Git Bash it needs "PyBank" removed in the line of code (See Below)
PyBank file main.py code in line 20 file_to_load = os.path.join("PyBank/Resources/budget_data.csv")
Only solve I could find was providing the absolute path, which was going to error out the code when anyone else ran it, please let me know if there's another solution.  This was the file hierarchy that was outlined in the requirements.

PyBank Challenge code explanation:
First I am importing the CSV file and setting the path for import as well as setting up the file export path 
In the Financial Analysis section I am setting up variables to store data further in the code when I start looping through all of the data rows
After initializing the variables I open the CSV file with the CSV reader and skip the header to go to the first row of data
I process the first row to store the data against the variables that were outlined above
Then I go into the for loop to run through the analysis on the subsequent rows
In the loop I calculate the change in previous and current rows of the data, through doing this I am able to check for the greatest increase and decrease
I move on to calculate the average change, using the sum of the change list as the total change value and dividing that by the number of rows (length of change list).
I setup a variable called "output" to hold all of the f strings that I want to print in my analysis results
I open the text file that I set up at the start of the code and write the final output (results) variable in the file

PyPoll Challenge code explanation:
First I am importing the CSV file and setting the path for import as well as setting up the file export path 
In the Election Data Analysis section I am setting up variables to store vote counts and candidates
Next I open the CSV file with the CSV reader and create a DictReader object to read the CSV file and convert each row into a dictionary
Moving to the for loop, this is looping through each row in the CSV file and counting each vote against the candidate name
The code moves to each row and evaluates the candidates name in the row to either store it to the correct candidate in the dictionary
Next we use the stored values for each candidate to determine a winner and create a "candidate_results" list to store the values to later use in our election results
I loop throught the list of candidates and votes they received, I use this to create a percentage variable and calculate the percent to total votes of every candidate.  The results of this is appended to the "candidate_results" in a f string format to be called in our election results
I created an election_results variable to hold the f strings to print all of the results.  I use the "candidate_results" list and note which index in the list I want printed, repeating this code 3x for the 3 candidates
I write the final results to a text file
