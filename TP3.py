
#BASE CODE FOR TERM PROJECT:

from cmu_graphics import * 

from Locations import * #current location, best move, where piece/AI have been 

from PIL import Image #for image import 
import textInput as textBox #for message and textbox 
import random #for random number for dice roll 
from class_AI import *  #AI piece
from CLASS_CARDS import * #player cards, winner cards 

#import class Cards 
def onAppStart(app):
    #Creates board and sets piece parameters 
    app.rows = 25
    app.cols = 24
    app.boardLeft = 265
    app.boardTop = 57
    app.boardWidth = 820
    app.boardHeight = 820
    app.cellBorderWidth = 1
    app.board = [([None] * app.cols) for row in range(app.rows)]
    app.mouseX = None 
    app.mouseY = None 
    app.moves = 0
    app.canMove = False 
    app.rectCenters = [ ]

    #############################IMAGES ##############################
    #https://www.pinterest.com/pin/437130707560630791/ 
    app.imageBoard = Image.open("gameboard.jpg") 
    app.imageBoard = CMUImage(app.imageBoard)
    #http://www.clker.com/clipart-red-card.html
    app.imageCards = Image.open("cards.jpg")  
    app.imageCards = CMUImage(app.imageCards)
    #https://www.istockphoto.com/illustrations/dice-clipart
    app.imageDice= Image.open('dice.jpg')
    app.imageDice= CMUImage(app.imageDice)
    app.imageNoteSheet= Image.open('notesheet.jpg')
    app.imageNoteSheet= CMUImage(app.imageNoteSheet)
    #(https://stock.adobe.com/images/help-web-button-customer-
    # service-support-faqs-sos-help-hotline/25949556)
    app.imageHelp= Image.open('helpbutton.jpg')
    app.imageHelp= CMUImage(app.imageHelp)
    app.instructions= Image.open('instructions.jpg')
    app.instructions= CMUImage(app.instructions)
    app.imageMakeGuess= Image.open('makeGuess.jpg')
    app.imageMakeGuess= CMUImage(app.imageMakeGuess)
    app.characterGuessImage= Image.open('guessPerson .jpg')
    app.characterGuessImage= CMUImage(app.characterGuessImage)
    app.farnamImage= Image.open('farnam.jpg')
    app.farnamImage= CMUImage(app.farnamImage)
    app.liamImage= Image.open('liam .jpg')
    app.liamImage= CMUImage(app.liamImage)
    app.andrewImage= Image.open('andrew .jpg')
    app.andrewImage= CMUImage(app.andrewImage)
    app.taylorImage= Image.open('taylor\.jpg')
    app.taylorImage= CMUImage(app.taylorImage)
    app.emiliaImage= Image.open('emilia.jpg')
    app.emiliaImage= CMUImage(app.emiliaImage)
    app.nextImage= Image.open('next.jpg')
    app.nextImage = CMUImage(app.nextImage)
    app.locationGuessImage= Image.open('location Guess.jpg')
    app.locationGuessImage = CMUImage(app.locationGuessImage)
    app.BakerImage= Image.open('baker.jpg')
    app.BakerImage = CMUImage(app.BakerImage)
    app.DohertyImage= Image.open('doherty.jpg')
    app.DohertyImage = CMUImage(app.DohertyImage)
    app.GatesImage= Image.open('gates.jpg')
    app.GatesImage = CMUImage(app.GatesImage)
    app.HuntImage= Image.open('hunt.jpg')
    app.HuntImage = CMUImage(app.HuntImage)
    app.PorterImage= Image.open('porter.jpg')
    app.PorterImage = CMUImage(app.PorterImage)
    app.PosnerImage= Image.open('posner.jpg')
    app.PosnerImage = CMUImage(app.PosnerImage)
    app.SorrelsImage= Image.open('sorells.jpg')
    app.SorrelsImage = CMUImage(app.SorrelsImage)
    app.TepperImage= Image.open('tepper.jpg')
    app.TepperImage = CMUImage(app.TepperImage)
    app.UCImage= Image.open('UC.jpg')
    app.UCImage = CMUImage(app.UCImage)
    app.WeaponGuessImage= Image.open('weapon Guess.jpg')
    app.WeaponGuessImage = CMUImage(app.WeaponGuessImage)
    #https://creazilla.com/nodes/3172779-wrench-clipart
    app.wrenchImage= Image.open('wrench.jpg')
    app.wrenchImage = CMUImage(app.wrenchImage)
    #https://creazilla.com/nodes/3227741-dagger-clipart
    app.daggerImage= Image.open('dagger.jpg')
    app.daggerImage = CMUImage(app.daggerImage)
    #https://pngtree.com/free-png-vectors/knife
    app.knifeImage= Image.open('knife.jpg')
    app.knifeImage = CMUImage(app.knifeImage)
    #https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.onlygfx.com%2F
    # bundle-rope-clipart-png-transparent%2F&psig=AOvVaw2DjIKWgm-ICGIQChbfC8m
    # B&ust=1682264992986000&source=images&cd=vfe&ved=0CAQQjB1qFwoTCIjJpM7rvf
    # 4CFQAAAAAdAAAAABAK
    app.ropeImage= Image.open('rope.jpg')
    app.ropeImage = CMUImage(app.ropeImage) 
    #https://clipartpng.com/?3167,bronze-candlestick-png-clip-art
    app.candlestickImage= Image.open('candlestick.jpg')
    app.candlestickImage = CMUImage(app.candlestickImage)
    #https://www.freeimages.com/icon/free-vector-yellow-post-
    # it-notes-with-push-pin-5385516
    app.imageGuessNote = Image.open('guess.jpg')
    app.imageGuessNote= CMUImage(app.imageGuessNote)
    #https://www.istockphoto.com/vector/note-papers-worksheet-notebook-writing
    # -sheet-eps-10-gm1182521271-332093093
    app.imageCheck = Image.open('notes.jpg')
    app.imageCheck= CMUImage(app.imageCheck)
    app.imagePlayers = Image.open('players.jpg')
    app.imagePlayers= CMUImage(app.imagePlayers)
    #https://www.cmu.edu/brand/brand-guidelines/visual-
    # identity/university-seal.html 
    #https://www.cmu.edu/brand/downloads/index.html
    #https://www.clipartmax.com/middle/m2i8A0K9H7A0K9i8_
    # magnifying-glass-clipart-magnification-clip-art-at-magnifying-glass/
    app.imageOpening = Image.open('opening.jpg')
    app.imageOpening= CMUImage(app.imageOpening)
    app.imageColors= Image.open('chooseColors.jpg')
    app.imageColors= CMUImage(app.imageColors)
    app.imageAccuse= Image.open('accuse.jpg')
    app.imageAccuse= CMUImage(app.imageAccuse)
    app.imageAccuseWarning= Image.open('accuseWarning.jpg')
    app.imageAccuseWarning= CMUImage(app.imageAccuseWarning)
    app.winningImage= Image.open('win.jpg')
    app.winningImage= CMUImage(app.winningImage)
    app.losingImage= Image.open('loss.jpg')
    app.losingImage= CMUImage(app.losingImage)
    app.messageOpponents= Image.open('oppMessage.jpg')
    app.messageOpponents= CMUImage(app.messageOpponents)
    app.hintButton = Image.open('hint.jpg')
    app.hintButton= CMUImage(app.hintButton)
    app.choiceHint= Image.open('selectHint.jpg')
    app.choiceHint = CMUImage(app.choiceHint)
    ###################      APP INFORMATION       ##########################
    app.AIpiece= [[0]]
    app.aiCol = 23
    app.aiRow= 7
    app.AIturn  = False
    app.aiLocation= AI(app.aiRow,app.aiCol)
    app.AIGuess= None

    #PEICE INFORMATION:
    app.piece = [[0]]
    app.pieceLeftCol = 0 
    app.pieceTopRow= 5
    app.dotColor = None
    app.roll = 0 
    app.cards= "None"
    #beginning images at interface 
    app.startImage= True 
    app.choosePlayers = False 
    app.chooseColor= False 
    app.currLocation= Locations(app.pieceTopRow, app.pieceLeftCol)
    #on click images 
    app.showCards = False 
    app.showHelp= False 
    app.diceRoll= False
    app.displayCharacters= False
    app.displayLocations = False  
    
    #what is guessed in string 
    app.guessCharacter= None 
    app.guessLocation = None 
    app.guessWeapon = None
    app.choseAccuse= False
    app.accuse = False 
    app.displayWeapons= False 
    app.displayGuess= False 
    app.guess= set()
    #notepad 
    app.showCheck= False 
    app.marks = False
    #checks whether is a win or a loss 
    app.win = False 
    app.loss = False 

    app.clickedMessage = False
    ##################HINTS###########################
    app.hintPress= False
    app.weaponHint = False 
    app.locationHint = False 
    app.characterHint = False 
    ################### PLAYER CARDS  #######################
    app.characterCards = ['Taylor', "Farnam", "Liam", "Andrew", "Emilia"]
    app.locationCards = ["Gates", "Posner", "UC", "Tepper", "Porter", "Baker", 
                        "Sorrels", "Hunt", "Doherty"]
    app.weaponCards= ['Rope', 'Candlestick', 'Knife', 'Wrench', 'Dagger']
    app.allCards= ['Taylor', "Farnam", "Liam", "Andrew", "Emilia","Gates",
                    "Posner", 
                   "UC", "Tepper", "Porter", "Baker", 
                        "Sorrels", "Hunt", 'rope', 'candlestick', 'knife', 
                        'wrench', 'dagger']
    
    app.randomPlayerNames= ["kai", "maya", "alexis", "nick", "caitlin", 
                            "geronimo", "ester", "caroline"]
    app.randomPlayerName= random.choice(app.randomPlayerNames)
    app.playerNum= 1 
    app.numCards= 18//app.playerNum
    app.showReturned = False
    app.showImageWin = False 
    app.showImageLoss = False 
     
    ##############################textBox############################
    app.text = ""
    print(len(app.text))
    app.letters= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    app.punc= '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    app.messageEntered = False
    app.finalMessage = None
    app.tokenWords= [("ally", "No I do not want to be ally"), 
                     ("cards", "show me what cards you have"), 
                     ('hello', "hello, opponent"),
                     ("win", "I will win, not you"),
                     ("lose", "you will lose, not me"),
                     ("who", "who am I? who are you?"),
                     ("you", "I am better than you"),
                     ("me", "you are crazy..."), 
                     ("better", "do you really think you can beat me?"),
                     ("ok", "are you mad?"), 
                     ("yes", "Thats fine. You are just going to lose now."),
                     ("no", "should I care?"), 
                     ("why?", "I have to focous on beating you"), 
                     ("goodbye", "bye bye"), 
                     ("hi", "hello, opponent"), 
                     ("bye", "Sayonara bebe"), 
                     ("hate", "hate is a strong word")]
    app.showResponse = False
def redrawAll(app):
    #drawImage(app.imageBoard,250,40, height= 850, width = 850)
    drawBoard(app)
    drawBoardBorder(app)
    drawImage(app.imageBoard,253,38, height= 850, width = 850)
    drawPlayerCircle(app)
    drawPiece(app)
    drawAIPiece(app)
    drawHelp(app)
    drawHint(app)
    drawCards(app)
    drawMessageOpponents(app)
    drawDice(app)
    drawMakeGuess(app)
    drawNote(app)
    drawAccuse(app)
    showReturned(app)
    
    drawLabel('click "ESC" to exit all pop ups ',675, 30, size=16)
    if app.startImage == True: #draws opening images 
        drawImage(app.imageOpening, 0,0, height = 950, width = 1500)
    if app.choosePlayers == True:#choose amount of players 
        drawImage(app.imagePlayers, 0,0,height= 950, width = 1500)
        #Cards(app.playerNum) #THIS IS FOR THE CARDS CLASS 
    if app.chooseColor== True: #choose the color you want your player to be 
        drawImage(app.imageColors, 0,0,height= 950, width = 1500)
    if app.showImageWin== True: #if u win 
        drawImage(app.winningImage, 0,0,height = 950,width = 1500) 
    if app.showImageLoss == True: #if u lose 
       drawImage(app.losingImage, 0, 0, height = 950,width = 1500) 
    if app.AIGuess !=None: #the guess the AI makes 
        drawAIGuess(app)
    if app.clickedMessage == True: #the open chat text box 
        drawRect(400,200,650,400, fill = "white")
        drawLabel("Type a message to opponents:", app.width/2, 
              app.height/3, size = 36)
        
        drawLabel(app.text, app.width/2, app.height/2, size = 36)
def drawMessageOpponents(app):#the message opponents emoji 
    drawImage(app.messageOpponents, 20, 700, height = 70, width = 200) 
    
def drawAccuse(app): #accuse emoji
    drawImage(app.imageAccuse, 1200,400, height= 80, width = 200) #if u accuse 
    if app.choseAccuse == True:
        drawRect(0,0,1500,1500, fill = "red")
        drawImage(app.imageAccuseWarning, 600,200, height = 600,width= 350)
def showReturned(app): #this is what the check of the guess us
     if app.showReturned == True:
          print("winning hand", app.cards.getWinningDeck())
          drawRect(0,0,1500,1500, fill = "red")
          drawLabel(f'{app.cards.checkGuess(app.guess)}', 650,300,size = 24)
          
def drawDice(app): #dice image and label of dice roll 
    drawImage(app.imageDice, 50, 360, height = 200, width = 180)
    if app.diceRoll == True:
        drawImage(app.imageDice, 0, 50, height = 300, width = 230)
        drawLabel(f" Dice Roll : {app.roll}", 160,330, size = 20)
def drawNote(app): #notepad and check mark 
    drawImage(app.imageNoteSheet, 1250,200, height = 80, width= 80)
    if app.showCheck== True:
        drawImage(app.imageCheck, 500,50, height = 700, width = 500)
        rectWidth = rectHeight = 20
        for i in range(len(app.rectCenters)):
            (cx, cy) = app.rectCenters[i]
            drawRect(cx - rectWidth/2, cy - rectHeight/2,
                rectWidth, rectHeight, fill='black')
        #how to delte the last rectangle 
        #how r u gonna draw a checkmark and have it remeber to stay up 
def checkDelete(app,mouseX,mouseY): #deletes the checkmark on the notes 
    # Cite - Homework 5: CLick to Delete 
    xPointMax= (mouseX + 12.5)
    xPointMin = mouseX - 12.5
    YPointMax = mouseY + 12.5
    YPointMin= mouseY - 12.5 
    
    for pointdel in range(len(app.rectCenters)):
        cx,cy = app.rectCenters[pointdel]
        if (cx- 25 <=mouseX <= cx+25):
            if (cy-25 <= mouseY <= cy +25):
                index = pointdel
    return index 
def drawPlayerCircle(app): #draws the other players circles 
    
    drawCircle(280,665,14, fill = "blue", border= "black")
    #drawCircle(1065,305,14, fill = "yellow", border= "black")
    drawCircle(587,859,14, fill = "green", border= "black")
    drawCircle(758,859,14, fill = "red", border= "black")
#def drawGuessSheet(app): #after making a guess, this is the confirmation     
def drawMakeGuess(app): #guess character cards pop up 
    drawImage(app.imageMakeGuess, 1200, 300, height= 80, width= 200)
    if app.displayCharacters == True: #only if chooses to guess 
        drawImage(app.characterGuessImage, 200 ,40, height = 820, width= 1000)
        drawImage(app.farnamImage, 300, 90, height = 300, width = 200)
        drawImage(app.taylorImage, 550, 90, height = 300, width = 200)
        drawImage(app.liamImage, 800, 90, height = 300, width = 200)
        drawImage(app.emiliaImage, 400, 550, height = 300, width = 200)
        drawImage(app.andrewImage, 700, 550, height = 300, width = 200)
        drawImage(app.nextImage, 940, 700, height = 90, width = 100)
    elif app.displayLocations== True: #only activates when true
        drawImage(app.locationGuessImage, 200 ,40, height = 820, width= 1000)
        drawImage(app.BakerImage, 210, 90, height = 200, width = 150)
        drawImage(app.DohertyImage, 420, 90, height = 200, width = 150)
        drawImage(app.UCImage, 620, 90, height = 200, width = 150)
        drawImage(app.GatesImage, 820, 90, height = 200, width = 150)
        drawImage(app.PosnerImage, 210, 550, height = 200, width = 150)
        drawImage(app.PorterImage, 400, 550, height = 200, width = 150)
        drawImage(app.TepperImage, 600, 550, height = 200, width = 150)
        drawImage(app.HuntImage, 800, 550, height = 200, width = 150)
        drawImage(app.SorrelsImage, 1000, 90, height = 200, width = 150)

        drawImage(app.nextImage, 1000, 700, height = 90, width = 150)
    elif app.displayWeapons == True:
        print("only display weapons should occur here ")
        drawImage(app.WeaponGuessImage, 200 ,40, height = 820, width= 1000)
        drawImage(app.candlestickImage, 280, 90, height = 300, width = 250)
        drawImage(app.ropeImage, 550, 90, height = 300, width = 250)
        drawImage(app.wrenchImage, 840, 90, height = 300, width = 250)
        drawImage(app.daggerImage, 350, 550, height = 300, width = 250)
        drawImage(app.knifeImage, 700, 550, height = 300, width = 250)
        drawImage(app.nextImage, 1000, 700, height = 90, width = 150)
    elif app.displayGuess== True: #this is never entering why? 
        ("YAHHAHAHAAHHAHAHAHAHHAHAH")
        drawImage(app.imageGuessNote, 200,40,height = 820, width = 1000)
        drawLabel(f'{app.guessCharacter}',400,300,size=60, font = "monostat")
        drawLabel(f'{app.guessLocation}', 400,450,size=60,font = "monostat")
        drawLabel(f'{app.guessWeapon}',400,650,size = 60,font = "monostat")
#DRAWS GRID AND PEICE UNDERNEATH 
def drawBoard(app):#draws to board for the amount of rows and cols 
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col, app.board[row][col])
def drawBoardBorder(app): # draw the board outline (with double-thickness):
  
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):#draws the individual cell 
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
            fill =color, border='black', #####
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col): #gets top left of cell 
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app): #gets cell size
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)
def drawHelp(app): #draws the instructions 
    drawImage(app.imageHelp, 1200,100, height = 80, width= 200)
    if app.showHelp== True:
        drawRect(0,0,1500,1500, fill = "red")
        drawImage(app.instructions, 600,200, height = 600, width= 350)
        drawLabel("Fill out your notepad -->", 1080, 230, size = 17)
        drawLabel("Guess -->", 1080,340,size = 20)
        drawLabel("Accuse(if your ready... -->)", 1050,450,size = 17)
        drawLabel("Click on a hint if you are stuck -->", 1050, 550, size = 15)
        drawLabel("Click on your cards to see your hand -->", 1048, 645, size = 17)
        drawLabel("<-- Click to roll the dice to move",420, 400, size = 20 )
        drawLabel("<--Chat with your opponent!", 400, 750, size = 20)
def drawPiece(app): #draws the piece
    rows= len(app.piece)
    cols= 1
    
    drawCell (app, app.pieceTopRow, app.pieceLeftCol, app.dotColor)
def drawAIPiece(app): #draws the AI piece on the board
    rows= len(app.AIpiece)
    cols= 1
    drawCell (app, app.aiRow, app.aiCol, "yellow")
def drawCards(app): #draws the cards you have bottom right corner 
    drawImage(app.imageCards, 1200, 600, height = 300, width = 180)
    if app.showCards == True:
        drawRect(250,40,850,800, fill = 'white')
        drawLabel(f'{app.cards.getPlayerCards()}', 700,400, size= 22)
def drawHint(app):#draws hint emoji 
    drawImage(app.hintButton, 1200,500, height = 80, width = 200)
    if app.hintPress== True:

        drawImage(app.choiceHint, 253,38, height= 850, width = 850) #choose what hint you want 
        if app.characterHint == True:
            drawRect(253,38,850, 850, fill = "white")
            drawLabel(f'{app.cards.hintCharacter()}', 800,500, size = 40)
        elif app.locationHint == True:
            drawRect(253,38,850, 850, fill = "white")
            drawLabel(f'{app.cards.hintLocation(app.pieceTopRow, app.pieceLeftCol)}', 750,500, size = 40)
        elif app.weaponHint== True:
            drawRect(253,38,850, 850, fill = "white")
            drawLabel(f'Solve the riddle:{app.cards.hintWeapon()}', 750,500, size = 40)
def onMousePress(app,mouseX,mouseY):
    if 20<mouseX<220 and 700<mouseY<900:
        app.clickedMessage = True #you want to wite message 
    if 1200<mouseX<1400 and 400<mouseY<480:
        app.choseAccuse= True #you want to accuse someone 
    if 1200<mouseX<1500 and 500<mouseY<580 and app.chooseColor == False: #you clicked the hint button 
        print(f'these r winners:{app.cards.getWinningDeck()}')
        app.hintPress = True 
    if 330 <mouseX<540 and 418<mouseY<520 and app.hintPress == True and app.locationHint== False and app.weaponHint == False:
#you clicked on character hint 
        app.characterHint= True 
    elif 600 <mouseX< 780 and 415<mouseY<520 and app.hintPress == True and app.characterHint == False and app.weaponHint == False:
        #you clicked a location hint 
        app.locationHint = True 
    elif 840 <mouseX<1020 and 415<mouseY<520 and app.hintPress == True:
        #you clicked a weapon hint 
        app.weaponHint = True
    if app.showCheck== True: #what draws the checks on the notepad 
        newCenterPoint = (mouseX, mouseY)
        delete= None
        for pointdel in range(len(app.rectCenters)):
            cx,cy = app.rectCenters[pointdel]
            if cx- 25 <=mouseX <= cx+25:
                if (cy-25 <= mouseY <= cy +25):
                    index = checkDelete(app, mouseX,mouseY)
                    delete = True 
        if delete== True:
            app.rectCenters.pop(index)
            #find the index that the duplicate is in 
        if delete != True:
            app.rectCenters.append(newCenterPoint)
    ###############This is just about the first images########################                                      
    if app.startImage== True :
        if 1017<mouseX<1300 and 420 <mouseY<520:
            app.choosePlayers = True 
            app.startImage = False #this should turn off the first image 
    elif app.choosePlayers == True: #choose how many players you want 
        if 220< mouseX<320 and 420<mouseY<560:
            app.playerNum = 2
            app.cards= Cards(app.playerNum)
        elif 530<mouseX<630 and 420<mouseY<560:
            app.playerNum = 3 
            app.cards= Cards(app.playerNum)
        elif 820<mouseX<920 and 420 <mouseY<560:
            app.playerNum = 4
            app.cards= Cards(app.playerNum)
        elif 1150<mouseX<1250 and 420<mouseY<520:
            app.playerNum = 5
            app.cards= Cards(app.playerNum) #sets the distribution of cards and winning deck 
            print(app.playerNum)
        if app.playerNum != 1:
            app.chooseColor= True
            app.choosePlayers = False
    elif app.chooseColor== True: #choose your player color 
        if 230 <mouseX< 400 and 360<mouseY<580:
            app.dotColor = "red"
        elif 540 <mouseX<720 and 360 <mouseY<580:
            app.dotColor = "blue"
        elif 850 <mouseX< 1050 and 380<mouseY<600:
            app.dotColor = "green"
        elif 1100 <mouseX< 1300 and 380<mouseY<600:
            app.dotColor = "brown"
        if app.dotColor != None:
            app.chooseColor = False 

    if 1200<mouseX<1380 and 600 <mouseY<900:
        app.showCards = True #you clciked to see your own cards 
    if 1200<mouseX<1350 and 100<mouseY<180:
        app.showHelp= True #you clicked on an instruction manual 
    if not 600< mouseX<950 and 200<mouseY<800:
        app.showHelp = False  #you clicked out 
    if 50 <mouseX< 230 and 300 <mouseY<500:
        dice(app) #you are rolling the dice to get the amount of moves so you can move 
        app.diceRoll= True
        app.canMove = True 
        app.turnOver = False
    if 1250<mouseX<1330 and 200 <mouseY< 280:
        app.showCheck= True #show notepad  
    if 1200 <mouseX<1400 and 300 <mouseY<380: #for when you are making a guess on characters 
        app.displayCharacters= True
        #onGuessPress(app, mouseX,mouseY) 
    if app.displayCharacters== True:
        if 300<mouseX<500 and 90<mouseY< 390:
            app.guessCharacter= 'Farnam'
        elif 550 <mouseX<750 and 90<mouseY<390:
            app.guessCharacter = 'Taylor'  
        elif 800 <mouseX<1050 and 90<mouseY<390:
            app.guessCharacter= 'Liam'
        elif 400<mouseX<600 and 550<mouseY< 850:
            app.guessCharacter= 'Emilia'
        elif 700<mouseX<900 and 550<mouseY< 850:
            app.guessCharacter = 'Andrew'
        if app.guessCharacter != None and 940<mouseX<1050 and 700<mouseY<780:
            app.displayCharacters = False #once you clciked enter for character 
            if app.accuse == True:# if you are accusing, shwo lcoations, if not, dont 
                app.displayLocations= True 
            app.guessLocation=getLocation(app.pieceTopRow, app.pieceLeftCol)#the guess location is based on where you are in the map 
            app.displayWeapons = True
    elif app.displayLocations == True: #if you are accusing you can sleect lcoation 
        if 210<mouseX<350 and 90<mouseY<290:
            app.guessLocation = "Baker" 
        elif 420<mouseX<570 and 90<mouseY<290:
            app.guessLocation = "Doherty"
        elif 620<mouseX<770 and 90<mouseY<290:
            app.guessLocation = "UC"
        elif 820<mouseX<970 and 90<mouseY<290:
            app.guessLocation = "Gates"
        elif 1000<mouseX<1150 and 90<mouseY<290:
            app.guessLocation = "Sorrels"
        elif 210 <mouseX< 360 and 550<mouseY<750:
            app.guessLocation= "Posner"
        elif 400 <mouseX< 550 and 550<mouseY<750:
            app.guessLocation= "Porter"
        elif 600 <mouseX< 750 and 550<mouseY<750:
            app.guessLocation= "Tepper"
        elif 800 <mouseX< 950 and 550<mouseY<750:
            app.guessLocation= "Hunt"
        if app.guessLocation != None and 100<mouseX<1150 and 700<mouseY<780:
            app.displayLocations= False 
            app.displayWeapons = True 
    elif app.displayWeapons== True: #weapon choice always pops up if you are guessing 
        if 280<mouseX<530 and 90<mouseY<390:
            app.guessWeapon = "Candlestick"
        elif 550<mouseX<800 and 90<mouseY<390:
            app.guessWeapon ="Rope"
        elif 840<mouseX<1090 and 90<mouseY<390:
            app.guessWeapon = "Wrench"
        elif 350<mouseX<600 and 550<mouseY<850:
            app.guessWeapon = "Dagger"
        elif 700 <mouseX<950 and 550<mouseY<850:
            app.guessWeapon = "Knife"
        if app.guessWeapon != None and 100<mouseX<1150 and 700<mouseY<780:#if u clicked enter 
            app.displayGuess= True
            app.displayWeapons = False
            
    elif (app.displayGuess == True and app.accuse == False and
           app.guessLocation != None and 
          607< mouseX< 912 and 780 < mouseY < 820): #if u made a guess and not an accusation 
        app.guess=set()
        app.guess.add(app.guessWeapon)
        app.guess.add(app.guessLocation)
        app.guess.add(app.guessCharacter) #creates et of everything you guessed 
        print("this is ur guess", app.guess)
        print(f' BRUH these r winners:{app.cards.getWinningDeck()}')
        print(f'{app.cards.playerCards}')
        print(f'this is whats returned {app.cards.checkGuess(app.guess)}')
        app.showReturned = True #show what cards u get back 
        app.turnOver= True
        app.canMove = False
        app.displayGuess= False #removes image of guess 
        app.moves = 0
        app.roll= 0
    elif (app.displayGuess == True and app.accuse == True and 
        607< mouseX< 912 and 780 < mouseY < 820): #they made an accusation
        app.guess = set()
        app.guess.add(app.guessWeapon)
        app.guess.add(app.guessLocation)
        app.guess.add(app.guessCharacter) #adds all to a guess of accusation 
        print(app.guess, app.cards.getWinningDeck())
        if isWin(app, app.guess, app.cards.getWinningDeck()):#only checks if win if an accuation 
            print(app.guess, app.cards.getWinningDeck())
            print("you won bro what ")
            app.win = True
            app.showImageWin = True #you win 
        elif not isWin(app, app.guess, app.cards.getWinningDeck()):
            app.loss = True
            app.showImageLoss= True #you lose 
    elif ((app.showImageWin== True or app.showImageLoss== True) and 
        (575<mouseX<915 and 780 <mouseY<880)): #if u clicked restart 
                onAppStart(app)
    if app.choseAccuse == True and 675<mouseX<880 and 645<mouseY<700:
        app.choseAccuse = False #how accuse is determined 
        app.accuse= True 
        app.displayCharacters= True

def dice(app): #dice roll 
    app.roll = random.randint(1,6) #chooses how many u get to roll 
    return app.roll    
   
def onKeyPress(app, key):
    app.currLocation= Locations(app.pieceTopRow, app.pieceLeftCol)
    if app.clickedMessage==True: #typing a message in text box 
        textBox.onKeyPress(app,key)
    print("row:", app.pieceTopRow, "col", app.pieceLeftCol)
    print("CURRENT LOCATION", app.currLocation)
    if key == 'left': #checks if move is legal, moves piece 
        if not app.currLocation.isWallLeft():
            movePiece(app, 0, -1)
    elif key=='right':#checks if move is legal, moves piece 
        if not app.currLocation.isWallRight():
            movePiece(app, 0, +1)
    elif key=='down':#checks if move is legal, moves piece 
        if not app.currLocation.isWallDown():
            movePiece(app, +1, 0)
    elif key == 'up':#checks if move is legal, moves piece 
        if not app.currLocation.isWallUp():
            movePiece(app, -1, 0)
    elif key == "escape": #resets board 
        app.choosePlayers = False 
        app.chooseColor= False 
        app.showCards = False 
        app.showHelp= False 
        app.hintPress= False
        app.displayCharacters= False
        app.displayLocations = False  
        app.displayWeapons= False 
        app.displayGuess= False 
        app.showCheck= False
        app.choseAccuse= False 
        app.showReturned = False
        app.AIGuess = None
        app.clickedMessage = False
        app.characterHint = False 
        app.weaponHint = False 
        app.locationHint = False
    elif key == '8':
         onAppStart(app)

def movePiece(app, drow, dcol): #how piece moves 

    if app.canMove == True: #if dice was rolled and not AI's turn 
        app.pieceLeftCol += dcol 
        app.pieceTopRow += drow
    app.moves += 1 
    if app.moves >=app.roll:
        app.turnOver= True 
        app.canMove = False 
        app.aiLocation.moveOver= False
        moveAIPiece(app)
        app.moves = 0
        app.roll= 0
         
    if app.pieceLeftCol == 23 and app.pieceTopRow == 5:
        app.pieceLeftCol= 1
        app.pieceTopRow= 19
    if app.pieceLeftCol ==0 and app.pieceTopRow == 3:
        app.pieceLeftCol = 18
        app.pieceTopRow= 23
    if not pieceIsLegal(app):
        app.pieceLeftCol -= dcol 
        app.pieceTopRow -= drow
        return False 
    return True 
def drawAIGuess(app):#what the AI guess is 
    drawRect(400,400,600,600, fill = "red")
    drawLabel(f'The AI Guess:{app.AIGuess}', 650,500, size = 20)
    common= app.AIGuess.difference(app.cards.getWinningDeck())
    drawLabel(f'AI recieved {len(common)} cards back', 650,580, size = 20)
def moveAIPiece(app):#how the Ai piece moves 
    if app.turnOver== True and (app.aiLocation.moveOver== False) and app.aiLocation.guessedLocation !=None: #if AI move is not false and if the players turn is over 
        #app.aiLocation.bestLocation()
        #(app.aiRow, app.aiCol)= app.aiLocation.goToRoom() #what room it is trying to go to 
        if app.aiLocation.inRoom():#if it is in a room it will make a guess 
                app.AIGuess = (app.aiLocation.makeGuess
                               (app.characterCards, app.weaponCards, app.cards.getWinningDeck()))
                if app.AIGuess== app.cards.getWinningDeck(): #has the AI win 
                    print("AI WON")
                    app.loss = True 
                    app.showImageLoss= True
                app.aiLocation.findRoom()#find out what room it is and pop from list of rooms to go to
    elif app.turnOver== True and (app.aiLocation.moveOver== False) and app.aiLocation.guessedLocation ==None: #if AI move is not false and if the players turn is over 
        app.aiLocation.bestLocation()
        (app.aiRow, app.aiCol)= app.aiLocation.goToRoom() #what room it is trying to go to 
        if app.aiLocation.inRoom():#if it is in a room it will make a guess 
                app.AIGuess = (app.aiLocation.makeGuess
                               (app.characterCards, app.weaponCards, app.cards.getWinningDeck()))
                if app.AIGuess== app.cards.getWinningDeck():
                    print("AI WON")
                    app.loss = True 

                app.aiLocation.findRoom()#find out what room it is and pop from list of rooms to go to 
        
def pieceIsLegal(app): #check to go through borders  
    for r in range (len(app.piece)):
        for c in range (1):
            boardRow = r + app.pieceTopRow 
            boardCol = c + app.pieceLeftCol 
            if (boardRow < 0 or boardRow >= app.rows or 
            boardCol < 0 or boardCol >= app.cols):
                return False 
    return True             
 
def getLocation(pieceTopRow, pieceLeftCol): #gets current location of peice 
    currentLocation= None
    if pieceTopRow in range(0, 4) and pieceLeftCol in range(0,7):
                    currentLocation = "Hunt" 
    elif pieceTopRow in range(1, 7) and pieceLeftCol in range(9,15):
                    currentLocation = "Gates"
    elif pieceTopRow in range(0, 6) and pieceLeftCol in range(17,24):
                    currentLocation = "Baker"
    elif pieceTopRow in range(6, 11) and pieceLeftCol in range(0,7):
                    currentLocation = "Sorells"
    elif pieceTopRow in range(9, 16) and pieceLeftCol in range(16,24):
                    currentLocation = "Tepper"
    elif pieceTopRow in range(12, 17) and pieceLeftCol in range(0,6):
                    currentLocation = "Doherty"
    elif pieceTopRow in range(19, 24) and pieceLeftCol in range(0,6):
                    currentLocation = "Porter"
    elif pieceTopRow in range(17, 24) and pieceLeftCol in range(8,16):
                    currentLocation = "UC"
    elif pieceTopRow in range(18, 24) and pieceLeftCol in range(18,24):
                    currentLocation = "Posner"    
    return currentLocation

def isWin(app,guess,winningDeck):#checks if there is a win 
    if guess== winningDeck:
        return True
    return False  

def main():
    runApp(width=1700, height=1700)

main()
