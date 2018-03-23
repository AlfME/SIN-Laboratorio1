"""
Script for verification of sudoku results.
"""
#imports
from collections import defaultdict

#aux
def storeInTable(field, value):
    #discard last entry on satisfiability
    if field == "sat":
        return
        
    #get array position and value
    line = int(field[1]) - 1
    column = int(field[2]) - 1
    
    val = int(value)
    
    #insert value to table
    table[column][line] = val

def initTable(squareSize, table):
    for i in range(squareSize * 3):
        table += [[-1 for j in range(squareSize * 3)]]

def printTable(table, squareSize):
    cur = ["" for i in range(len(table))]
    
    j = 0
    
    for col in table:
        i = 0
        
        for field in col:
            if j % squareSize == 0:
                cur[i] += "|"
            
            cur[i] += " " + str(field) + " |"
                
            i += 1
    
        j += 1      
    
    j = 0
    for line in cur:
        print(line)
        
        if (j+1) % squareSize == 0:
            print()
            
        print()
        j += 1

def verifyDict(dict):
	if len(dict.keys()) != 9:
		return False

	for i in dict.items():
		if i[1] != 1:
			return False
		
		if not i[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
			return False
	
	return True
		
def verifyTable(table, squareSize):
    accLines = [defaultdict(int) for i in range(len(table))]
    accSquares = [defaultdict(int) for i in range(9)]
    
    j = 0
    
    for col in table:
        accCol = defaultdict(int)
        i = 0
        
        for field in col:   
            accCol[field] += 1
            
            accLines[i][field] += 1
            
            sqr = 3 * (i // squareSize) + j // squareSize
            accSquares[sqr][field] += 1
            
            i += 1
        
        #invalid column
        if not verifyDict(accCol):
            return False
    
        j += 1
        
    #invalid lines
    for dictline in accLines:
        if not verifyDict(dictline):
            return False
    
    #invalid squares
    for dictsqr in accSquares:
        if not verifyDict(dictsqr):
            return False
            
    return True
        
        
#init result table
table = []
initTable(3, table)
printTable(table, 3)
        
#get file
inputfile = open('./Results/resultados_sudoku.txt')
outputfile = open('./Results/verifyres.txt')

#skip until solution
for line in inputfile:
    if line[:8] == "SOLUTION":
        break;

#get solution line
raw = inputfile.readline();

#get each field with value and store it in result
accF = ""
accV = ""
state = "blanc"

for c in raw:
    if state == "field":
        if c == " ":
            state = "equal"
        else:
            accF += c
    elif state == "equal":
        if c == " ":
            state = "value"
    elif state == "value":
        if c == " ":
            state = "blanc"
            
            storeInTable(accF, accV)
            
            accF = ""
            accV = ""
        else:
            accV += c
    elif state == "blanc":
        if c != " ":
            state = "field"
            accF += c
    else:
        print("Error - unreachable state")
        
		
printTable(table, 3)

print("The result is valid:", verifyTable(table, 3))

outputfile.write("The result is valid:" + str(verifyTable(table, 3)));
