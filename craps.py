#include the "randint" function from python's "random" module
from random import randint
# pointOn is the variable that says the point is set or not
pointOn=False
point=0
roundOver=False
playerbank = 10000
playerbet = 0
housewins = False
playerwins = False

name = raw_input("What is your name? ")
print "Hello " + name + ". " + "Your bank is at: " + str(playerbank)
# playerbet = raw_input("What is your wager? ")

#saying there are two dice d1+d2 it's adding the random number
def roll():
    global pointOn, point, roundOver, housewins, playerwins
    d1=randint(1,6)
    d2=randint(1,6)
    value = d1+d2
    print "Player Rolls a " + str(value)

    #this is saying if the pointOn is NOT TRUE (False) then...
    if not pointOn:
        if value==2 or value==3 or value==12:
            housewins = True
            print "House wins "
            roundOver=True

        elif value==7 or value==11:
            playerwins = True
            print "Player wins."
            roundOver=True
        else:
            point = value
            pointOn = True
            print "The point has been set to " + str(point)
#this is saying that if the roll is what the point was set to player wins or if its a 7 house wins
    else:
        if value==point:
            playerwins = True
            print "Player wins."
            roundOver=True
        elif value==7:
            housewins = True
            print "House wins."
            roundOver=True



#this rolls until point is set or rolls 7
# while not roundOver:
#     roll()




#       end of the roll function

# startgame function
def startgame():
    global pointOn, point, roundOver, playerbank, playerbet, playagain,housewins,playerwins
    pointOn = False
    roundOver = False
    housewins = False
    playerwins = False
    point = 0
    print "You have " + str(playerbank) + " in your bank."
    playerbet = raw_input("Place your bet: ")

    while not roundOver:
        roll()

    if housewins:
        playerbank = playerbank - int(playerbet)

    if playerwins:
        playerbank = playerbank + int(playerbet)

    playagain = raw_input("Do you want to play again? Y or N? ")

playagain = "Y"

while playagain=="Y":
        startgame()

print "Thanks for playing"
