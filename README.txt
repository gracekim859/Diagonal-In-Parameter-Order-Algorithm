# Diagonal-In-Parameter-Order-Algorithm
Diagonal In-Parameter-Order is a alternative approach to the current In-Parameter-Order algorithm (IPO). In simple terms, both algorithms work to expand an already existing covering array by a column through the use of horizontal and veritcal growth. A covering array is organized into columns(k) and rows(n) containing a certain number of values (v). However, in order to be considered a covering array, the array must essentially cover all possible interactions between t-number (also called the strength) of and between all the columns. It is also important to note that prior to either algorithm, the starting array must be a valid covering array. 
Below is in example of a covering array where k = 3, v = 2, and t = 2. 

|0|0|1|  
|0|1|0|
|1|0|0|
|1|1|1|
Every iterations or combination of the values 0 and 1 are covered between each pair of the three columns.  

In the original IPO algorithm, this is its strategy 
1.) begin with a covering array 
     |0|0|   k = 2
     |0|1|   v = 2
     |1|0|   t = 2
     |1|1| 
2.) begin horizantal growth by adding a column (array physically grows horizantally)
     |0|0| |  
     |0|1| | 
     |1|0| | 
     |1|1| | 
3.) The order of execution of the empty slots of the array are approached differently depending on the strategy, but for simplicity, this algorithm will execute it in order logically. Therefore, looking at the slot located at (3,1) of the array, this algorithm plugs in the value that will cover the most interactions needed for the array to become a covering array. 
     |0|0| |<- inserting (1) will cover the interactions (0, ,1) ( ,0,1)
     |0|1| |   inserting (0) will cover the interactions (0, ,0) ( ,1,0)           
     |1|0| |    *please keep in mind that the strength of this covering array is 2, therefore we are accounting for interactions between two columns)*
     |1|1| | 