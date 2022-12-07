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

IN-PARAMETER-ORDER ALGORITHM:
In the original IPO algorithm, this is its strategy. 
1.) begin with a covering array 
     |0|0|1|  k = 3
     |0|1|0|  v = 2
     |1|0|0|  t = 2
     |1|1|1| 
2.) begin horizantal growth by adding a column (array physically grows horizantally) *note that adding this column makes it insufficient to be a covering array*
     |0|0|1| |
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
3.) The order of execution of the empty slots of the array are approached differently depending on the strategy, but for simplicity, this algorithm will execute in
logival order. Therefore, looking at the slot located at (4,1) of the array, this algorithm plugs in the value that will cover the most interactions needed for the
array to become a covering array. 
     |0|0|1| |<- inserting (1) will cover the interactions (0, , ,1) and ( ,0, ,1) and ( , ,1,1)
     |0|1|0| |   inserting (0) will cover the interactions (0, , ,0) and ( ,0, ,0) and ( , ,1,0) 
     |1|0|0| |   *please keep in mind that the strength of this covering array is 2, therefore we are accounting for interactions between two columns*
     |1|1|1| |  
4.) Since inserting both values will cover the same number of iteractions, the algorithm will randomly choose a value to insert.
     |0|0|1|1|
     |0|1|0| |
     |1|0|0| |
     |1|1|1| |  
5.) Then it will move down to the next slot, repeating step 3. 
     |0|0|1|1|
     |0|1|0| |<- inserting (1) will cover the interactions ( ,1, ,1) and ( , ,0,1)
     |1|0|0| |   inserting (0) will cover the interactions (0, , ,0) and ( ,1, ,0) and ( , ,0,0)
     |1|1|1| |   *we are ommiting the interaction (0, , ,1) because it has already been covered by the first iteration of the horzantal growth.*
6.) In this case, the value 0 covers more interactions; therefore, a 0 will be placed in that slot.
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0| |
     |1|1|1| |
7.) If this process continues, the resulting array is below
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|<-both values had the same number of interactions; therefore, the value is randomly chosen
     |1|1|1|1|<-inserting (1) will cover more interactions    
8.) Once the slots are all filled out in this manner, the horizantal growth is complete. Next is the vertical growth. The vertical stage is where the interactions
that have yet to be covered are inserted. Therefore, it must identify the interactions that need to be covered.
For this current array, the interactions that need to be covered are ( , ,0,1) and ( , ,1,0)
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|
     |1|1|1|1|
9.) Next insert a row at the bottom of the array one by one to include the missing interactions.
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|
     |1|1|1|1|
     |x|x|0|1|<-covers the interaction ( , ,0,1)
     |x|x|1|0|<-covers the interaction ( , ,1,0)
     *the "x" are "don't care" value placements where it does not matter which value is put in that position
10.)The last step would be condensing the array vertically in places where the values and "don't care" values line up. In this case, there is no overlap; therefore,
the final array is:
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|
     |1|1|1|1|
     |x|x|0|1|
     |x|x|1|0|

At the end of the algorithm, the final covering array will vary from time to time due to the variance of inserting random values in certain steps along with the state
or order of the initial covering array. 

DIAGONAL IN-PARAMETER-ORDER ALGORITHM:
The Diagonal IPO algorithm utilizes the horizontal and vertical growth aspects of the IPO but implements them concurrently. 
This is the strategy:
1.) begin with a covering array (using the final array from the previous example)
     |0|0|1|  k = 3
     |0|1|0|  v = 2
     |1|0|0|  t = 2
     |1|1|1|
2.) begin horizantal growth by adding a column (array physically grows horizantally) *note that adding this column makes it insufficient to be a covering array*
     |0|0|1| |
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
3.) Similarly, the order of execution of the empty slots of the array are approached differently depending on the implementation, but for simplicity, this algorithm
will execute it in order logically. Therefore, looking at the slot located at (4,1) of the array, this algorithm plugs in the value that will cover at least a certain percentage of the remaining uncovered interaction, for this example, this percentage will be 25% If no values fit this minimum, this slot will remain empty. 
     Total remaining interactions: 12
     Minimum: 3
     |0|0|1| |<- inserting (1) will cover the interactions (0, , ,1) and ( ,0, ,1) and ( , ,1,1) satisfying the minimum
     |0|1|0| |   inserting (0) will cover the interactions (0, , ,0) and ( ,0, ,0) and ( , ,1,0) satisfying the minimum
     |1|0|0| |   
     |1|1|1| |
4.) Since both values satisfy the minimum, the algorithm will randomly select a value to place in the slot. 
     |0|0|1|1|
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
5.) Then it will switch over to vertical growth, adding a row to the current array
     |0|0|1|1|
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
     | | | | |
6.) The row is randomly generated with values. If the interaction it covers is equal to or exceeds the average, then it will place the values in the slots. 
     Randomly Generated Row: (0,1,1,1)      -> covers 2 interactions
     Average coverage = (uncovered interactions)/(v^t): 8/4 = 2
     |0|0|1|1|
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
     | | | | |
7.) Since the row generated satisfies the condition, it will add this row to the array. 
     |0|0|1|1|
     |0|1|0| |
     |1|0|0| |
     |1|1|1| | 
     |0|1|1|1|
8.) The algorithm will then jump back to horizantal growth where it left off.
     Total remaining interactions: 7
     Minimum: 2
     |0|0|1|1|   
     |0|1|0| |<- inserting (1) will cover no iteractions not satisfying the minimum
     |1|0|0| |   inserting (0) will cover the interactions (0, , ,0) and ( ,1, ,0) and ( , ,0,0) satisfying the minimum
     |1|1|1| |
     |0|1|1|1|
9.) Since only the value 0 satisfies the minimum, a 0 will be placed in that slot. 
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0| |
     |1|1|1| | 
     |0|1|1|1|
10.) The algorithm will repeat the same sequence, moving onto the vertical growth again. 
     Randomly Generated Row: (1,0,0,1)      -> covers 1 interactions
     Average coverage = (uncovered interactions)/(v^t): 4/4 = 1
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0| |
     |1|1|1| | 
     |0|1|1|1|
     | | | | |
11.) Since the row generated satisfies the condition, it will add this row to the array
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0| |
     |1|1|1| | 
     |0|1|1|1|
     |1|0|0|1|
12.) Horizantal growth again...
     Total remaining interactions: 3
     Minimum: 1
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0| |<- inserting (1) will cover no iteractions not satisfying the minimum
     |1|1|1| |   inserting (0) will cover the interactions (1, , ,0) and ( ,0, ,0) satisfying the minimum
     |0|1|1|1|
     |1|0|0|1|
 13.) Since only the value 0 satisfies the minimum, a 0 will be placed in that slot. 
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|
     |1|1|1| | 
     |0|1|1|1|
     |1|0|0|1|
 14.) Veritcal growth again...
     Randomly Generated Row: (1,1,0,0)      -> covers 1 interactions
     Average coverage = (uncovered interactions)/(v^t): 1/4 = 1
     |0|0|1|1|      |0|0|1|1|
     |0|1|0|0|      |0|1|0|0|
     |1|0|0|0|      |1|0|0|0| 
     |1|1|1| |  ->  |1|1|1| | 
     |0|1|1|1|      |0|1|1|1|
     |1|0|0|1|      |1|0|0|1|
     | | | | |      |1|1|0|0|
 15.) At this point, all interactions are covered; therefore, any empty slots will be filled with "dont care" values, making our final array this:
     |0|0|1|1|
     |0|1|0|0|
     |1|0|0|0|
     |1|1|1|x| 
     |0|1|1|1|
     |1|0|0|1|
     |1|1|0|0|
 Some cases were not covered in this specific example:
     a) in the case where during horizantal growth, no values satisfy the minimum, the algorithm will leave that slot empty and move to the next one until one slot is 
     filled. 
     b) in the case where the randomly generated row during veritcal growth does not satisfy the condition, then it would keep generating random rows until a one 
     satisfies it. 
     
 Repository:
 In this repository there is a Covering Array Validator, which returns true if an array is covering and false if it is not. In addition, there is an implementation of
 Diagonal IPO where it reads an array in a text file and expands it with the users input of the number of columns in the starting array along with the v and t values.
 It is important to note that both programs read from a text file with the name "test.txt" containing an array with a specific format. Please refer to the "test.txt"
 file to see this format. Lastly, the Diagonal IPO algorithm includes the covering array validator at the end to confirm that the resulting array is covering. 
