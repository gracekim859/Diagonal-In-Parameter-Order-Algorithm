import itertools

def makeArray(textfile):
    covArray = []
    with open(textfile) as f:
        for i in range(4):
            if i == 1:
                k = int(f.readline())
            if i == 2:
                v = int(f.readline())
            if i == 3:
                t = int(f.readline())
        for line in f:
            row = []
            for num in line:
                if num != '\n':
                    row.append(int(num))
            covArray.append(row)
    f.close()
    return (covArray, k, v, t)

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

#rray1, k, v, t = makeArray('coveringArray.txt')
array = [[0,0,1], [0,1,0], [1,0,0], [1,1,1]]
print(isValid(array, 3, 2, 2))