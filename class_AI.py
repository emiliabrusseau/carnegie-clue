import random

class AI:
    def __init__(self, row, col):
        self.row = row 
        self.col = col
        self.listOfLocations = [("Hunt",3,6), ("Sorells", 8,6), 
                                ("Doherty", 15,5), ("Porter", 19,4),
                                ("Gates",6,11), ("Baker", 5, 17),
                                ("Tepper", 9, 17), ("Posner", 17,19),
                                ("UC",16,14)] 
        self.doorLst= [(3,6),(8,6),(15,5),(19,4),(6,11),(5,17),(9,17),
                       (17,19),(16,14)]

        self.moveOver = False
        self.guess = set()
        self.characterCards = ['Taylor', "Farnam", "Liam", "Andrew", "Emilia"]
        self.weaponCards= ['Rope', 'Candlestick', 'Knife', 'Wrench', 'Dagger']
        self.guessedCharacter = None
        self.guessedLocation= None 
        self.guessedWeapon = None 
    def bestLocation(self): #this finds the best location
        bestRow = None 
        bestCol = None 
        leastMoves = 1000
        for (room, brow,bcol) in self.listOfLocations:
            print(room,brow,bcol)
            moves = (abs(brow- self.row)+ abs(bcol -self.col)) #how many total moves 
            print(room, moves)
            if moves <leastMoves: #checks if smallest moves 
                bestRow = brow 
                bestCol = bcol 
                bestRoom= room
                leastMoves = moves
                moves = 0#sets moves if better 
        self.bestRow= bestRow
        self.bestCol = bestCol
        self.bestRoom = bestRoom
        return  
    def inRoom(self):
        if (self.row, self.col) in self.doorLst: #checks if AI in a room 
            return True 
        
    def findRoom(self): #deletes room if it was there 
        for i in range(len(self.listOfLocations)):
            if((self.bestRoom, self.bestRow,self.bestCol)==
            self.listOfLocations[i-1]):
                self.listOfLocations.pop(i-1)
        return f'{self.listOfLocations}' 

    def goToRoom(self): #movement of AI peice around the board based off of best location to be
        if self.guessedLocation != None:
            return #ai is already in the best location 
        rowMoves = abs(self.bestRow-self.row)

        colMoves = abs(self.col - self.bestCol)
        amtMoves = 0 
        roll = random.randint(1,6)
        while (amtMoves <= roll) and self.moveOver== False:
            for r in range(colMoves):
                if amtMoves == roll:
                    self.moveOver = True
                    return (self.row,self.col)
                if self.col > self.bestCol:
                    self.col -= 1
                    amtMoves += 1
                elif self.col < self.bestCol:
                    self.col += 1
                    amtMoves += 1
            for j in range(rowMoves):
                print("momoves", amtMoves)
                if amtMoves == roll:
                    self.moveOver = True
                    return (self.row,self.col)
                elif self.row < self.bestRow:
                    self.row+=1
                    amtMoves += 1
                elif self.row > self.bestRow:
                    self.row -=1
                    amtMoves += 1
            self.moveOver = True 
            if amtMoves == roll:
                self.moveOver = True
                return (self.row,self.col)
            self.moveOver = True
            return (self.row, self.col)
        return (self.row, self.col)
    
    def __repr__(self):
        return f' this is ur row: {self.row} and this is ur col {self.col}'
    def makeGuess(self, characters, weapons, winningDeck): #AI makes educated guesses 
        self.guess = set()
        c = random.choice(characters)
        w= random.choice(weapons)
        if c in winningDeck and self.guessedCharacter == None:
            self.guessedCharacter= c
            self.guess.add(self.guessedCharacter)
        elif self.guessedCharacter == None and c not in winningDeck:
            ("YOU GOT THE RIGHT CHARACTER", self.guessedCharacter)
            #keep guessing C everytime 
            self.guess.add(c)
        elif self.guessedCharacter != None:
            self.guess.add(self.guessedCharacter)
        if w in winningDeck and self.guessedWeapon == None: #u guessed it right, u always guess it again 
            ("YOU GOT THE RIGHT WEAPON", self.guessedWeapon)
            self.guessedWeapon = w
            self.guess.add(self.guessedWeapon)
        elif self.guessedWeapon == None and w not in winningDeck: #and w not in winning deck 
            self.guess.add(w)
        elif self.guessedWeapon != None: #u guessed it right once so u keep adding 
            self.guess.add(self.guessedWeapon)
        if self.guessedLocation == None:
            self.guess.add(self.bestRoom)
        if self.bestRoom in winningDeck or self.guessedLocation != None:
            self.guessedLocation = self.bestRoom 
            self.guess.add(self.guessedLocation)
        if self.guessedCharacter != None and self.guessedWeapon != None and self.guessedLocation !=None:
            print("ai won")
        return self.guess
    '''
    def theGuess(self, totCards):
        if len(guess)== 2:
            self.guess.add(self.bestRoom)
            return self.guess
        else:
            for char in range(len(totCards)):
                if totCards[char] in self.characterCards:
                    characterGuess = 
                    '''
                    


tester = (AI(5,3))

print(tester.bestLocation())
print(tester.moveOver)
print("_____________________")
print(tester.goToRoom())
print(tester.moveOver)
print(tester.findRoom())



