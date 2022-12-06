from bdb import Breakpoint
import random
import copy
import itertools
import math

#read text file and coverts it to an array of arrays
def makeArray(textfile):
    covArray = []
    with open(textfile) as f:
        for line in f:
            row = []
            for num in line:
                if num != '\n':
                    row.append(int(num))
            covArray.append(row)
    f.close()
    return covArray

#Diagonal IPO Start
def diagonalIPO(array, k, t, v):
    k+=1 #adding column first
    uncovered = set(itertools.product(itertools.combinations(range(k-1), t-1), itertools.product(range(v), repeat = t)))

    #adding in an "empty" column
    for row in array: 
        row.append(-1)
    
    newarray = horizontal(array,k,uncovered)
    #return the newly generated array
    return newarray

#Horizontal Growth
def horizontal(a, k,uncov): 
    while len(uncov)!= 0: 
        for row in range(len(a)):
            if a[row][k-1] != -1: #if its already inputted, skip
                break
            for val in range(v):
                a[row][k-1] = val
                total = len(uncov)
                ifgood = copy.deepcopy(uncov)
                for cols, vals in uncov:
                    count = 0
                    ncols = list(cols) + [k-1] #adding last column that was not accounted for
                    ncols = tuple(ncols)
                    check = []
                    for col in ncols: 
                        check.append(a[row][col])
                    check = tuple(check)
                    if check == vals:
                        count +=1 
                        ifgood.remove((cols, vals))
                if (count/total)*100 < 8:
                    a[row][k-1] = -1
                else:
                    uncov = ifgood
                    break
        #if there is still uncovered interactions...
        if len(uncov)!= 0:
            a, k, uncov = vertical(a, k, uncov)
    #return final array 
    return a

#Vertical Growth
def vertical(a, k, uncov):
    #must go above this average to be sufficient as new row
    avg = math.ceil(len(uncov)/v**t)

    #make random row
    newrow = []
    for i in range(k):
        newrow.append(random.randint(0,v-1))
    plusrow = copy.deepcopy(a)
    plusrow.append(newrow)
    ifgood = copy.deepcopy(uncov)

    #boolean to see if this row is "good enough"
    good = False

    #keep generated random row and checking until it goes over average AKA "good enough"
    while good != True:
        #used same method
        for cols, vals in uncov:
            count = 0
            ncols = list(cols) + [k-1] #adding last column that was not accounted for
            ncols = tuple(ncols)
            check = []
            for col in ncols: 
                check.append(plusrow[len(a)][col])
            check = tuple(check)
            if check == vals:
                count +=1 
                ifgood.remove((cols, vals))
        #checking if it covers over avg
        if count>=avg:
            good = True
            a = plusrow
            uncov = ifgood
        #else create new random row
        else:
            newrow = []
            for i in range(k):
                newrow.append(random.randint(0,v-1))
            plusrow = copy.deepcopy(a)
            plusrow.append(newrow)
            ifgood = copy.deepcopy(uncov)
    #return new a and new uncov
    return (a, k, uncov)

#Copied from Validator
def isValid(covArray, k, v, t):
    for cols in itertools.combinations(range(k), t): #goes through all possible combos of columns depending on t
        s = set()                                    #makes new set every time to check every case independently
        for row in range(len(covArray)):             #goes through every row
            tup = [ ]                                #create a list to add on each value of the columns in the combo
            for col in cols:                         #loops through the columns in the combo (in the big for loop)
                tup.append(covArray[row][col])       #appends every value into the list
            s.add(tuple(tup))                        #adds every row into the set and does not include any repeats
            if len(s) == v**t:                       #checks if all the needed values are in there (all possible combos)
                break                                #continues to next combo if the length matches (does not have to check other rows cuz all the needed values are there)
        else:
            return False                             #returns False if something does not match 
    return True

#OUPUTS:
array= makeArray('test.txt')
k = int(input("Enter number of columns in current array: "))
v = int(input("Enter the number of values you want: "))
t = int(input("Enter the strength: "))
fine = diagonalIPO(array, k, t, v)
for row in fine:
    print(row)
print(isValid(fine, k, v, t)) #checking if final array is covering array