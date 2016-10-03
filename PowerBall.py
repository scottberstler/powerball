"""
The below code was written to complete the following project:

Below is a project that you can choose the best way to implement in python.
Post your code to GitHub and send us a link to the repository, if you don't have a GitHub account, you sign up for one at https://github.com/join
Powerball story:
As a Greenphire employee I would like to add my favorite 6 numbers to consider for a Powerball entry ticket so that I can win 1 billion dollars.


Capture the name of the employees entering the number.
The first 5 favorite numbers will need to be in the range of 1 to 69 and unique. (remember that this is a drawing so there cannot be duplicates in this range of 5 numbers)
6th favorite number will need to be in the range of 1 to 26 and flagged as the 6th Powerball number.
Keep count of each individual favorite number provided to determine which numbers to use in our final winning number. (i.e. count the duplicates).
Retrieve the max count of each unique duplicate number and use them as the Powerball numbers.
if there is a tie based on the max counts randomly select the tied number.
Display all employees with their corresponding number entries.
Display the final Powerball number based on the requirements above.

Sample output:
Enter your first name: Wade
Enter your last name: Wilson
select 1st # (1 thru 69): 12
select 2nd # (1 thru 69 excluding 12): 20
select 3rd # (1 thru 69 excluding 12 and 20): 23
select 4th # (1 thru 69 excluding 12, 20, and 23: 56
select 5th # (1 thru 69 excluding 12, 20, 23, and 56: 30
select Power Ball # (1 thru 26): 25


Wade Wilson 15 26 33 60 34 Powerball: 16
Frank Castle 15 26 34 56 61 Powerball: 16


Powerball winning number:
15 26 34 55 63 Powerball: 16


ver 1.0.0 by Scott Berstler - 10.03.2016
"""

# known issues:
#   if the user hits enter without entering data within the first 2 prompts, the script will throw an exception.
# Note: Due to availability, this script has only been tested on Microsoft Windows 10 with Python 2.7.11 


import getArgs as ga
import getPb as pb
import sys
class PowerBall():
    rev = '1.0.0'
    pyName = "PowerBall.py"
    
    def __init__(self):
        # get arguments from the command line
        doneGetting = ga.get().getall()
        # track inputs and calculate the Powerball #s
        pb.makecount(doneGetting)
        # format and print output
        self.out(pb.values.returnlist, doneGetting)


    def out(self, win, person):
        # format and print output
        for i in person.itervalues():
            sys.stdout.write(str(i[0]) + " " + str(i[1]) + " "  + str(i[2]) + " "  + str(i[3]) + " " + str(i[4]) +\
                             " "  + str(i[5]) + " " + str(i[6]) + " Powerball: " + str(i[7])  + "\n")
            sys.stdout.flush()
        sys.stdout.write("\n\nPowerball winning number:\n" + str(win[0]) + " " + str(win[1]) + " " + str(win[2]) +\
                         " " + str(win[3]) + " " + str(win[4]) + " Powerball: " + str(win[5]))
        sys.stdout.flush()
if __name__ == "__main__":
    PowerBall()



