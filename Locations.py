from cmu_graphics import *
class Locations:
    def __init__(self, row,col): #this whole function checks legality of moves based off of wall location 
        self.row = row 
        self.col = col
    def isWallUp(self): #checks if the wall is UP 
        if self.row == 4: #Hunt
            if self.col in range(0,6):
                return True
        elif self.row == 10:
            if self.col in range(1,3): #sorells
                return True
            elif self.col in range(4,6):
                return True
        elif self.row == 17: #doherty
            if self.col in range(0,6):
                return True  
        elif self.row== 16: #tepper
            if self.col in range(19,24):
                return True 
        elif self.row == 15: #Tepper
            if self.col in range(16,19):
                return True
        if self.row == 6: #Baker
            if self.col in range(18,24):
                return True 
        elif self.row==6:
            if self.col in range(9,11):
                return True
            elif self.col in range(13,15):
                return True
        else:
            return False  

    def isWallDown(self):
        if self.row==5: #sorrels
            if self.col in range(0,6):
                return True
        elif self.row == 11:#doherty
            if self.col in range(2,6):
                return True 
        elif self.row == 17:
            if self.col in range(0,5):
                return True
        elif self.row == 16:#the UC 
            if self.col in range(10,14):
                return True
            elif self.col == 8:
                return True 
            elif self.col == 14:
                return True
            elif self.col == 7:
                return True 
            elif self.col==14:
                return True 
        elif self.row == 17: #posner
            if self.col in range(20,24):
                return True 
        elif self.row == 8: #tepper
            if self.col in range(18,24):
                return True 
        else:
            return False
    def isWallLeft(self):
        if self.col == 7: #hunt
            if self.row in range(0,4):
                return True
        elif self.col == 15:#gates
            if self.row in range(0,7):
                return True
        elif self.col == 6: #doherty
            if self.row in range(12,15):
                return True
            elif self.row in range(15,16):
                return True 
        if self.col ==6: #porter
            if self.row in range(19,24):
                return True
        if self.col == 16: #UC
            if self.row in range(19,22):
                return True 
            elif self.row in range(16, 18):
                return True 
    def isWallRight(self):
        if self.col==8:
            if self.row in range(0,2):#gates
                return True
            elif self.row in range(5,7):
                return True
        elif self.col == 16: #baker
            if self.row in range(0,6):
                return True 
        elif self.col==15:#tepper
            if self.row in range(9,12):
                return True
            elif self.row in range(13,15):
                return True 
        elif self.col == 7: #uc 
            if self.row in range(19,24):
                return True
            elif self.row in range(16,18):
                return True 
        elif self.col == 17: #posner
            if self.row in range(17, 13):
                return True 
             
        
            
    def __repr__(self):
        return f'row:{self.row}, col:{self.col}'



