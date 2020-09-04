"""
Author: Jason Burnell
Algorithms Project 1: Accumulation
Updated:2/16/20
Description: Inputs a filename that is possibly populated with positive and negative integers.
Outputs the sum of the positive integers while ignoring the negative integers and stops if -999 is present in the file.
"""

def function():
    # Get filename from stdin 
     filename = input()
     # Open the file and read in its contents
     with open(filename) as f:
        # convert contents to array  
        numbers = [int(i) for i in f]
        start = numbers[0]
        # set index as end of file int but continue if index is not found in array
        x = -999 
        index = numbers.index(x) if x in numbers else None
        sum = 0
        num = 0
        # if nothing is in file, print empty
        if not start:
            print("EMPTY")
        # handles the case when EOF is the first entry 
        elif numbers[1] == x:
            print("EMPTY")
        # array contains data
        elif numbers:      
            # loop to iterate through array starting after first number to end of file, then sum and print the positive integers
            for num in numbers[1:index]:
                if num >= 0:
                    sum += num
            print(sum)
function()
