import random
import time
def returnConflicts(gameMap):
    n = len(gameMap)
    c = [[0 for N in range(n)] for N in range(n)]
    for i in range(n):
        for j in range(n):
                
            for k in range(0, n):
                if(gameMap[i][k]==1):
                    c[i][j] += 1        ## horiziontally 
                if(gameMap[k][j]==1 and i != k):
                    c[i][j] += 1
            for k in range(1, n):
                if(i-k >= 0 and j + k < n):   ## (-, +)
                    if gameMap[i-k][j+k] == 1:
                        c[i][j] += 1
                if i+k < n and j - k >= 0:
                    if gameMap[i+k][j-k] == 1:
                        c[i][j] += 1
                if i-k >= 0 and j-k >= 0:
                    if gameMap[i-k][j-k] == 1:
                        c[i][j] += 1
                if i+k < n and j+k < n:
                    if gameMap[i+k][j+k] == 1:
                        c[i][j] += 1            
    return c

def improve(gameMap, queensloc, conflicts):
    
    
    queen = queensloc[random.randint(0, len(queensloc)-1)]
    x,y = queen

    min = conflicts[x][y]
    minIndex = y

    for c in range(0, len(conflicts[x])-1):
        if conflicts[x][c] < min :
            min = conflicts[x][c]
            minIndex = c
        elif conflicts[x][c] == min :
            coinToss = random.randint(0,2)
            if coinToss == 0:
                min = conflicts[x][c]
                minIndex = c
    
    gameMap[x][y] = 0
    gameMap[x][minIndex] = 1
    
    # if(conflicts[x][y] != 0):
    #     min = conflicts[x][y]
    #     k = 0
    #     minIndex = y
    #     for c in conflicts[x]:      ## conflicts[x] = [5, 7, 2] 
    #         if(c < min):
    #             minIndex = k
    #         elif(c == min and random.randint(0,2) == 1):
    #             print(c)
    #             print(min)
    #             minIndex = k
    #         k+=1
    #     gameMap[x][y] = 0
    #     gameMap[x][minIndex] = 1


    return gameMap

def getLeastConflict(conflicts,row):
    min = 4
    cords = [99,99]
    for i in range(0,conflicts[row].__len__()):
        if(conflicts[row][i] < min):
            cords[0] = row
            cords[1] = i
            min = conflicts[row][i]
    return cords[1]
    

def myImprove(gameMap, queensloc, conflicts):
    queen = queensloc[random.randint(0, len(queensloc)-1)]
    x,y = queen
    rand1 = random.randint(0,gameMap[0].__len__()-1)
    rand2 = random.randint(0,gameMap[0].__len__()-1)

    for i in range(0,gameMap[rand1].__len__()):
        if(gameMap[rand1][i] ==1):
            loc = getLeastConflict(conflicts,rand1)
            #print("Row: ",rand1," Col: ",loc)
            gameMap[rand1][i] =0;
            gameMap[rand1][loc] = 1 ;

    return gameMap;

def randomImprove(gameMap, queensloc, conflicts):
    changed = False
    queen = queensloc[random.randint(0, len(queensloc)-1)]
    x,y = queen
    row = col = 0
    
    while(not changed):
        row = random.randint(0,gameMap[0].__len__()-1)
        col = random.randint(0,gameMap[0].__len__()-1)
        if( not queensloc.__contains__((row,col))):
            queensloc.remove((x,y))
            queensloc.append((row,col))
            gameMap[x][y] = 0
            gameMap[row][col] = 1
            changed = True

   
    return gameMap
            

    
    

def getQueensLoc(gameMap,queensloc):
    queensloc = []
    for i in range(0,gameMap.__len__()):
        for j in range(0,gameMap[i].__len__()):
            if(gameMap[i][j] == 1):
                queensloc.append((i,j))
            
    return queensloc

def printBoard(board):
    for i in range(0,board.__len__()):
        print(board[i])
                       
                       
def isStuck(queensloc,oldQueenloc):
    stuck = True;
    for i in range(0,queensloc.__len__()) :
        if(queensloc[i] != oldQueenloc[i]):
            stuck = False
        else:
            stuck = True
    return stuck
def generateRRGameMap(gameMap,queensloc): ## Random Row based game map
    for i in range(0, n):
        rand = random.randint(0,n-1)
        gameMap[i][rand] = 1
        queensloc.append((i,rand))
    mapProp = [gameMap,queensloc]
    return mapProp

def generateRGameMap(gameMap,queensloc): # Totally Random game map
    
    while(queensloc.__len__() <= gameMap.__len__()-1):
        row = random.randint(0,n-1)
        col = random.randint(0,n-1)
        randomCord = (row,col)
        if(queensloc.__contains__(randomCord)):
            continue
        queensloc.append(randomCord)
        gameMap[row][col] =1
    
    mapProp = [gameMap,queensloc]
    
    return mapProp
          
        
    

    
def NQueens(t,n):
    
    #gameMap = [[1 for n in range(5)] for n in range(5)
    
        
        
    queensloc = []
    gameMap = [[0 for N in range(n)] for N in range(n)] ## INITILIZLAZE GAMEMAP TO ZEROES
##    for i in range(0, n):
##        rand = random.randint(0,n-1)
##        gameMap[i][rand] = 1
##        queensloc.append((i,rand))
    gameMap,queensloc = generateRRGameMap(gameMap,queensloc)

    conflicts = returnConflicts(gameMap)
    
    solved = False
    threshcnt = 0;
    while(not solved):
        #isconflict = false
        gameMap = myImprove(gameMap, queensloc, conflicts)
        oldQueenloc = queensloc
        queensloc = getQueensLoc(gameMap,queensloc)        
        conflicts = returnConflicts(gameMap)
        

        stuck = isStuck(queensloc,oldQueenloc)
        if(stuck):
            threshcnt = threshcnt+1
            #print("ITERATION#",t," Stuck THRSH=",threshcnt)
        if(threshcnt == thresh):
            #print("ITERATION#",t," TERMINATING ",threshcnt,"/",thresh)
            return True
            

       # printBoard(gameMap)
        #printBoard(conflicts)
        #print(queensloc)
        
        c = 0
        for qx, qy in queensloc:
            #print(conflicts[qx][qy])
            if conflicts[qx][qy] > 1:
                c+=1
        if(c == 0):
             solved = True
             endTime = time.time()
             #print("------------",n,"Queen PROBLEM SOLVED------------/n Time Took: ",endTime-startTime," seconds only!" ) 
             #printBoard(gameMap)
             #printBoard(conflicts)
             #print(queensloc)
             return False




if __name__ == "__main__":
    totalTime = 0
    t=0;
    n = int(input("ENTER N:\n"))
    thresh = 3
    
    ## repition is a variable that specifies how many time the problem will be sovled
    repition = 500
    ## cnt is a variable that will incerment unitll it reaches the repition value
    cnt = 0
    for cnt in range(0,repition):
        startTime = time.time()
        while (NQueens(t,n)):
           t = t+1
           #print("Repition # ",cnt)
        totalTime = totalTime + time.time() - startTime
    avgTime = totalTime / repition

    print("Average time of ",repition," repititions is secs",avgTime)
    


