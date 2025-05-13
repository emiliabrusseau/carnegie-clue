# Super simple text input demo
# mdtaylor 4/18
from cmu_graphics import *

'''def onAppStart(app): #################PLACED IN TP#######################
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
                     ("you", "I am better than you")]
    app.showResponse = False'''
def onKeyPress(app, key):
    app.finalMessage = None
    if app.showResponse == True and key in app.letters:
        app.text = "" #rests message 
    app.showResponse = False#deletes current message if user starts typing again 
    if key in app.letters:#if letter upper or lower case 
        app.text += key #adds 
    if key == "space":
        app.text += " "
    if key in app.punc:#reads punctuation 
        app.text += key
    if key == "backspace":
        app.text = app.text[:-1]#deletes 
    elif key == "enter": #if enter returns message 
        app.finalMessage= app.text
        app.text = ""
        app.messageEntered = True
        readMessage(app)
def readMessage(app): #reponds based off of token word 
    for token in app.finalMessage.split(" "):
        print(token)
        for phrase in app.tokenWords:
            print(token, phrase)
            (word,response)= phrase
            if token == word:
                app.showResponse = True
                if app.showResponse == True:
                    app.text = response

        


'''def redrawAll(app):
    drawLabel("Type a message to opponents:", app.width/2, 
              app.height/3, size = 36)
    drawLabel(app.text, app.width/2, app.height/2, size = 36)
    
runApp(width=600, height=600)'''