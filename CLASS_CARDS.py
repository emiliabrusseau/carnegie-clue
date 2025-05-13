import random 
#winner cards and players cards:
import copy
class Cards: #this is the districution of cards 
    def __init__(self, playerCount):
        self.playerCount= playerCount
        self.cardNumber= 18//playerCount #determines card number by total and player count 
        self.playerCards = set()
        self.winnerDeck = set()
        self.characterCards = ['Taylor', "Farnam", "Liam", "Andrew", "Emilia"]
        self.locationCards = ["Gates", "Posner", "UC", "Tepper", "Porter", "Baker", 
                        "Sorrels", "Hunt", "Doherty"]
        self.weaponCards= ['Rope', 'Candlestick', 'Knife', 'Wrench', 'Dagger']
        self.allCards=['Taylor', "Farnam", "Liam", "Andrew", "Emilia","Gates",
                    "Posner", "UC", "Tepper", "Porter", "Baker", 
                        "Sorrels", "Hunt", 'Rope', 'Candlestick', 'Knife', 
                        'Wrench', 'Dagger']
        choiceCharacter= random.choice(self.characterCards)
        self.allCards.remove(choiceCharacter)
        choiceLocation= random.choice(self.locationCards)
        self.allCards.remove(choiceLocation)
        choiceWeapon = random.choice(self.weaponCards)
        self.allCards.remove(choiceWeapon)
        self.winnerDeck.add(choiceCharacter)
        self.winnerDeck.add(choiceLocation)
        self.winnerDeck.add(choiceWeapon) #creates winner deck
        print("WINNERS", self.winnerDeck)
        for i in range(self.cardNumber): #gets main players cards 
            choices = random.choice(self.allCards)
            self.playerCards.add(choices)
            self.allCards.remove(choices) #makes sure main player doesnt see own returned when making guesses 
        self.randomPlayerNames= ["Kai", "Maya", "Alexis", "Caitlin", 
                        "Geronimo", "Ester", "Caroline"]
        self.randomPlayerName= random.choice(self.randomPlayerNames)
        self.listOfLocations = [("Hunt",3,6), ("Sorells", 8,8), 
                                ("Doherty", 15,5), ("Porter", 19,4),
                                ("Gates",6,11), ("Baker", 5, 17),
                                ("Tepper", 9, 17), ("Posner", 17,19),
                                ("UC",16,14)] #list of doors for each location for hints 
        self.doorLst= [(3,6),(8,8),(15,5),(19,4),(6,11),(5,17),(9,17),
                       (17,19),(16,14)] #just a list of the doors 
    def getPlayerCards(self): #the cards the player gets 
        dict= {}
        weapons = []
        locations= []
        characters = []
        for card in self.playerCards:
            if card in self.weaponCards:
                weapons.append(card)
                dict["Weapon"] = weapons 
            elif card in self.locationCards:
                locations.append(card)
                dict["Location"]= locations
            elif card in self.characterCards:
                characters.append(card)
                dict["Character"]= characters
        return dict

    def __hash__(self):
        return hash(str(self))
    
    def getWinningDeck(self): #returns the winner 3 cards 
        return self.winnerDeck
    
    def hintWeapon(self): #hitn for the wepaon based off of a riddle 
        for card in self.winnerDeck:
            print(card)
            if card in self.weaponCards:
                if card== "Wrench":
                    return "Two sided spork"
                if card == "Rope":
                    return """A beginning and an end have I.
                    I can wind or be taught. 
                    Im easier to climb when Im full of knots."""
                if card == "Candlestick":
                    return """light me with a match, 
                    I choose to shine in the black"""
                if card == "Knife":
                    return "I am sharp, but not bright"
                if card == "Dagger":
                    return " A weapon I am. I cut and ram."
    def hintCharacter(self):#determines a character hint based off of winner character and a fact 
        for card in self.winnerDeck:
            if card in self.characterCards:
                if card == "Andrew":
                    return "Scottish born"
                if card == "Liam":
                    return "15-112 TA"
                if card == "Taylor":
                    return "My parents and I formed a non-profit"
                if card == "Emilia":
                    return "One often describe her as a CREATOR"
                if card == "Farnam":
                    return "A president of a very small population"
                
    def hintLocation(self, row, col): #determines best location for player to go to based off of current location 
        bestRow = None 
        bestCol = None 
        leastMoves = 1000
        lstOfLocs = copy.deepcopy(self.listOfLocations)
        for (room, brow,bcol) in lstOfLocs:
            moves = (abs(brow- row)+ abs(bcol - col))
            if moves <leastMoves:
                bestRow = brow 
                bestCol = bcol 
                bestRoom= room
                leastMoves = moves
                moves = 0      
        lstOfLocs.pop(0)
        self.bestRow= bestRow
        self.bestCol = bestCol
        self.bestRoom = bestRoom
        return f'The next best room for you to enter is: {bestRoom}'
                

    def allCards(self):
        return self.allCards
    
    def checkGuess(self, guess): #checks the guess and returns if cards not in winner cards 
        print(guess)
        Gdict= {}
        s = ""
        Gweapons = []
        Glocations= []
        Gcharacters = []
        for card in guess:
            if card in self.characterCards and card in self.allCards:
                print("all cards", self.allCards)
                CharCard = card
                Gcharacters.append(CharCard)
                Gdict["Character"]= Gcharacters
                s += (f'''  {random.choice(self.randomPlayerNames)} showed you the card {CharCard}!''')
            elif card in self.locationCards and card in self.allCards:
                LocCard = card 
                Glocations.append(LocCard)
                Gdict["Location"]= Glocations
                s += (f'''  {random.choice(self.randomPlayerNames)} showed you the card {LocCard}!''')
            elif card in self.weaponCards and card in self.allCards:
                WeapCard = card 
                Gweapons.append(WeapCard)
                Gdict["Weapon"] = Gweapons 
                s += (f'  {random.choice(self.randomPlayerNames)} showed you the card {WeapCard}!')
        if len(Gdict)== 0:
            return "No cards in deck match guess "
        else:
            return f'{s}' #return dictionary of cards 
    
    def isWin(self, accusation): #checks if it is a win 
        if self.winnerDeck == accusation:
            return True 
        return False 
    def __eq__(self, other):
        return (isinstance(other, Cards)) 
    def __str__(self):
        print(f'the amount of cards{self.cardNumber} because {self.playerCount}')




p1 = Cards(3)
#print(p1)
print(p1.getPlayerCards())
#print(p1.hint())
print("hi winners", p1.getWinningDeck())
print("hey baes", p1.hintWeapon())
guess= ('Gates',"Taylor", "Wrench")
print(p1.checkGuess(guess))
print(p1.hintLocation(7,9))
