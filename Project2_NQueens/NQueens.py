import random
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
                       
                       
                    

def NQueens():
    #gameMap = [[1 for n in range(5)] for n in range(5)
    n = int(input("ENTER N:\n"))
    queensloc = []
    gameMap = [[0 for N in range(n)] for N in range(n)] ## INITILIZLAZE GAMEMAP TO ZEROES
    for i in range(0, n):
        rand = random.randint(0,n-1)
        gameMap[i][rand] = 1
        queensloc.append((i,rand))

    conflicts = returnConflicts(gameMap)
   
    solved = False
    while(not solved):
       
        gameMap = improve(gameMap, queensloc, conflicts)
        queensloc = getQueensLoc(gameMap,queensloc)
        conflicts = returnConflicts(gameMap)

        printBoard(gameMap)
        printBoard(conflicts)
        print(queensloc)
        
        c = 0
        for qx, qy in queensloc:
            print(conflicts[qx][qy])
            if conflicts[qx][qy] > 1:
           
                c+=1
        if(c == 0):
             solved = True
             printBoard(gameMap)
             printBoard(conflicts)




if __name__ == "__main__":


    NQueens()


