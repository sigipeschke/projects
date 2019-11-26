from LibrarySimpleGraphicsTicTacToe import *
import random

#Setting Up The Game
#This will keep track which player keys into what square
player1sq1 = "x/1" #Player 1 is always X
player1sq2 = "x/2"
player1sq3 = "x/3"
player1sq4 = "x/4"
player1sq5 = "x/5"
player1sq6 = "x/6"
player1sq7 = "x/7"
player1sq8 = "x/8"
player1sq9 = "x/9"
player2sq1 = "o/1" #Player 2 is always O
player2sq2 = "o/2"
player2sq3 = "o/3"
player2sq4 = "o/4"
player2sq5 = "o/5"
player2sq6 = "o/6"
player2sq7 = "o/7"
player2sq8 = "o/8"
player2sq9 = "o/9"

#The Board
background("grey")
setFill("white")
setOutline("black")
setFont("Times","12","bold")
square1 = rect(5,215,100,100)
square1text = text(15,225,"1")
square2 = rect(110,215,100,100)
square2text = text(120,225,"2")
square3 = rect(215,215,100,100)
square3text = text(225,225,"3")
square4 = rect(5,110,100,100)
square4text = text(15,120,"4")
square5 = rect(110,110,100,100)
square5text = text(120,120,"5")
square6 = rect(215,110,100,100)
square6text = text(225,120,"6")
square7 = rect(5,5,100,100)
square7text = text(15,15,"7")
square8 = rect(110,5,100,100)
square8text = text(120,15,"8")
square9 = rect(215,5,100,100)
square9text = text(225,15,"9")

#Starting The Game
diceroll = "roll" #Assigns input 'roll' to diceroll
#print()
player1 = input("Player 1, please enter your name: ") #Assigns following input to player1
player2 = input("Player 2, please enter your name: ") #Assigns following input to player2
print(player1,"shall roll for a number between 1-100 to see who goes first.")
while (input("Type 'roll' to generate a number. ").lower() != diceroll):        #Type roll [not case sensitive thanks to .lower()] to continue
    print("Nah nah, can't trick me. Please type 'roll' to generate a number.")
dice1 = random.randint(1,100)  #Generate random integer between 1 and 100
print(player1,"rolled",dice1)
print(player2,"shall roll for a number between 1-100 to see who goes first.")
while (input("Type 'roll' to generate a number. ").lower() != diceroll):        #Type roll [not case sensitive thanks to .lower()] to continue
    print("Nah nah, can't trick me. Please type 'roll' to generate a number.")
dice2 = random.randint(1,100)  #Generate random integer between 1 and 100
print(player2,"rolled",dice2)
if dice1>dice2:
    print(player1,"shall go first.")
    print("To place an X/O, enter in the form 'tile/number'. Since",player1,"is X, they will enter 'x/1' to place an X on tile 1.")
if dice1<dice2:
    print(player2,"shall go first.")
    print("To place an X/O, enter in the form 'tile/number'. Since",player2,"is O, they will enter 'o/1' to place an O on tile 1.")
if dice1==dice2: #If the same number is rolled, player 2 will roll again
    print("You both rolled the same number, rock papers scissors best out of 1 to see who goes first")
    print("To place an X/O, enter in the form 'tile/number'. Since",player1,"is X, they will enter 'x/1' to place an X on tile 1.")
    
n = 1 # The value n will count number of valid turns made
sq1_inputnumber = 0 #These will count if there was an input made to the square
sq2_inputnumber = 0
sq3_inputnumber = 0
sq4_inputnumber = 0
sq5_inputnumber = 0
sq6_inputnumber = 0
sq7_inputnumber = 0
sq8_inputnumber = 0
sq9_inputnumber = 0
sq1player1_input = 0 #These will distinguish between which player has an X/O in the square
sq2player1_input = 0
sq3player1_input = 0
sq4player1_input = 0
sq5player1_input = 0
sq6player1_input = 0
sq7player1_input = 0
sq8player1_input = 0
sq9player1_input = 0
sq1player2_input = 0
sq2player2_input = 0
sq3player2_input = 0
sq4player2_input = 0
sq5player2_input = 0
sq6player2_input = 0
sq7player2_input = 0
sq8player2_input = 0
sq9player2_input = 0

#//////////////// Note for Dr. Stephenson, the following while loop is where I was told a function would be better than creating an if for each individual case
while n<=9:  ##Since a maximum of nine turns can be played only nine inputs will be allowed
    setColor("black")
    turn = input("Place your X/O: ").lower()
################################################################## Player 1 Inputs 
    if turn == player1sq1: # Check if the input corresponds to sqaure one and was made by Player 1
        sq1_inputnumber += 1 # Add a value of 1 to Square 1 to say that this spot is taken
        if sq1_inputnumber >= 2: # If another input has been made to this square this will run
            print("Cannot place an X on this tile!")
        else: # If no input has been made to this square this will run
            n += 1 # Add one to the number of VALID turns made
            polygon(30,230,90,290,80,300,20,240) #Place X
            polygon(90,240,30,300,20,290,80,230)
            print(player2+"'s turn.")
            sq1player1_input += 1 #Add a value of 1 to Square 1 by Player 1 so that it can check for winning moves
    if turn == player1sq2: ## Note, the rest repeat this first if statement just for each individual input
        sq2_inputnumber += 1
        if sq2_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(135,230,195,290,185,300,125,240)
            polygon(195,240,135,300,125,290,185,230)
            print(player2+"'s turn.")
            sq2player1_input += 1
    if turn == player1sq3:
        sq3_inputnumber += 1
        if sq3_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(240,230,300,290,290,300,230,240)
            polygon(300,240,240,300,230,290,290,230)
            print(player2+"'s turn.")
            sq3player1_input += 1
    if turn == player1sq4:
        sq4_inputnumber += 1
        if sq4_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(30,125,90,185,80,195,20,135)
            polygon(90,135,30,195,20,185,80,125)
            print(player2+"'s turn.")
            sq4player1_input += 1
    if turn == player1sq5:
        sq5_inputnumber += 1
        if sq5_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(135,125,195,185,185,195,125,135)
            polygon(195,135,135,195,125,185,185,125)
            print(player2+"'s turn.")
            sq5player1_input += 1
    if turn == player1sq6:
        sq6_inputnumber += 1
        if sq6_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(240,125,300,185,290,195,230,135)
            polygon(300,135,240,195,230,185,290,125)
            print(player2+"'s turn.")
            sq6player1_input += 1
    if turn == player1sq7:
        sq7_inputnumber += 1
        if sq7_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(30,20,90,80,80,90,20,30)
            polygon(90,30,30,90,20,80,80,20)
            print(player2+"'s turn.")
            sq7player1_input += 1
    if turn == player1sq8:
        sq8_inputnumber += 1
        if sq8_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(135,20,195,80,185,90,125,30)
            polygon(195,30,135,90,125,80,185,20)
            print(player2+"'s turn.")
            sq8player1_input += 1
    if turn == player1sq9:
        sq9_inputnumber += 1
        if sq9_inputnumber >= 2:
            print("Cannot place an X on this tile!")
        else:
            n += 1
            polygon(240,20,300,80,290,90,230,30)
            polygon(300,30,240,90,230,80,290,20)
            print(player2+"'s turn.")
            sq9player1_input += 1
################################################################## Player 2 Inputs
    if turn == player2sq1:
        sq1_inputnumber += 1
        if sq1_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(20,230,70,70)
            setColor("white")
            ellipse(25,235,60,60)
            print(player1+"'s turn.")
            sq1player2_input += 1
    if turn == player2sq2:
        sq2_inputnumber += 1
        if sq2_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(125,230,70,70)
            setColor("white")
            ellipse(130,235,60,60)
            print(player1+"'s turn.")
            sq2player2_input += 1
    if turn == player2sq3:
        sq3_inputnumber += 1
        if sq3_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(230,230,70,70)
            setColor("white")
            ellipse(235,235,60,60)
            print(player1+"'s turn.")
            sq3player2_input += 1
    if turn == player2sq4:
        sq4_inputnumber += 1
        if sq4_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(20,125,70,70)
            setColor("white")
            ellipse(25,130,60,60)
            print(player1+"'s turn.")
            sq4player2_input += 1
    if turn == player2sq5:
        sq5_inputnumber += 1
        if sq5_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(125,125,70,70)
            setColor("white")
            ellipse(130,130,60,60)
            print(player1+"'s turn.")
            sq5player2_input += 1
    if turn == player2sq6:
        sq6_inputnumber += 1
        if sq6_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(230,125,70,70)
            setColor("white")
            ellipse(235,130,60,60)
            print(player1+"'s turn.")
            sq6player2_input += 1
    if turn == player2sq7:
        sq7_inputnumber += 1
        if sq7_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(20,20,70,70)
            setColor("white")
            ellipse(25,25,60,60)
            print(player1+"'s turn.")
            sq7player2_input += 1
    if turn == player2sq8:
        sq8_inputnumber += 1
        if sq8_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(125,20,70,70)
            setColor("white")
            ellipse(130,25,60,60)
            print(player1+"'s turn.")
            sq8player2_input += 1
    if turn == player2sq9:
        sq9_inputnumber += 1
        if sq9_inputnumber >= 2:
            print("Cannot place an O on this tile!")
        else:
            n += 1
            ellipse(230,20,70,70)
            setColor("white")
            ellipse(235,25,60,60)
            print(player1+"'s turn.")
            sq9player2_input += 1
####################################################### Check if someone has won the game
    if sq1player1_input == 1 and sq2player1_input == 1 and sq3player1_input ==1: #Each individual if statement here is the 8 possible winning lines.
        print("Just kidding!", player1,"has won the game!")
        n += 9 #Make n greater than 9 in order to end the game.
    if sq4player1_input == 1 and sq5player1_input == 1 and sq6player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq7player1_input == 1 and sq8player1_input == 1 and sq9player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq7player1_input == 1 and sq4player1_input == 1 and sq1player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq8player1_input == 1 and sq5player1_input == 1 and sq2player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq9player1_input == 1 and sq6player1_input == 1 and sq3player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq7player1_input == 1 and sq5player1_input == 1 and sq3player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
    if sq9player1_input == 1 and sq5player1_input == 1 and sq1player1_input ==1:
        print("Just kidding!", player1,"has won the game!")
        n += 9
############################ Repeat above for player 2
    if sq1player2_input == 1 and sq2player2_input == 1 and sq3player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq4player2_input == 1 and sq5player2_input == 1 and sq6player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq7player2_input == 1 and sq8player2_input == 1 and sq9player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq7player2_input == 1 and sq4player2_input == 1 and sq1player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq8player2_input == 1 and sq5player2_input == 1 and sq2player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq9player2_input == 1 and sq6player2_input == 1 and sq3player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq7player2_input == 1 and sq5player2_input == 1 and sq3player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
    if sq9player2_input == 1 and sq5player2_input == 1 and sq1player2_input ==1:
        print("Just kidding!", player2,"has won the game!")
        n += 9
        
print ("Hope you enjoyed!")
