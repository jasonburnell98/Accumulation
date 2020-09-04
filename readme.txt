create a readme.txt that explains your solution at a high level. 
Inside your readme.txt file, make sure you clearly explain the 
algorithmic runtime of your program in terms of Big O.

The following algorithm was used to solve this problem:
    1. Import the necessary file containing the sequence of integers
    2. Convert the contents in the file into an array to manipulate later on.
    3. Create an index in the array which will be equal to -999 (indicating end of file)
        if index is not present in array, simply set it to -1 to be ignored
    4. Set sum variable to zero
    5. Check to see if array (file) is empty or populated
    6. If array is populated, move to step 7, else print empty
    7. Loop through array, ignoring the first number in array
         (First number indicates quantity of values and is not necessarily needed in our calculation)
    8. Sum all positive numbers and ignore negative numbers while in loop
    9. Stop summation when -999 is encountered or reached end of array
    10. Print sum

We will break the problem down into cost and time to determine the algorithmic runtime. 
The cost is broken up into the variables used in our program such as index = c1, sum = c2, etc. 
In our program we only have 1 loop that will iterate through the 1D array, this is linear, 
and therefore can be shown T(sum) = Cn + C' where C and C' are equal to the different costs of the function(C1,C2,...)
Since our loop is n+1, and our sum is n, we have come up with Cn + C',
and in terms of the asymptotic notation the algorithmic runtime would be O(n)

