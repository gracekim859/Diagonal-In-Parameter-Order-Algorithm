# Diagonal-In-Parameter-Order-Algorithm
Diagonal In-Parameter-Order is a alternative approach to the current In-Parameter-Order algorithm (IPO). In simple terms, both algorithms work to expand an already
existing covering array by a column through the use of horizontal and veritcal growth. A covering array is organized into columns(k) and rows(n) containing a certain
number of values(v). However, in order to be considered a covering array, the array must essentially cover all possible interactions between t-number(also known as
the strength) of and between all the columns. It is also important to note that prior to either algorithm, the starting array must be a valid covering array. 
Below is in example of a covering array where k = 3, v = 2, and t = 2. 

     |0|0|1|  
     |0|1|0|
     |1|0|0|
     |1|1|1|
Every iterations or combination of the values 0 and 1 are covered between each pair of the three columns. 

Important Variables:
k: number of columns
v: number of values
t: strength


     
 Repository:
 In this repository there is a Covering Array Validator, which returns true if an array is covering and false if it is not. In addition, there is an implementation of
 Diagonal IPO where it reads an array in a text file and expands it with the users input of the number of columns in the starting array along with the v and t values.
 It is important to note that both programs read from a text file with the name "test.txt" containing an array with a specific format. Please refer to the "test.txt"
 file to see this format. Lastly, the Diagonal IPO algorithm includes the covering array validator at the end to confirm that the resulting array is covering. 
