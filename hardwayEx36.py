import random

#############
## Classes ##
#############

##  This class defines an instance of the Game.
##  Defines a list of rooms for every game.
##  For the current game, sets score and rooms
##  visited to 0.
##  Allows modification of instance variables
##  with its built in functions.

class Game(object):
    rooms = ["Enter", "Pentagram", "Triangle", "Square", "Circle", "Star", "Dungeon", "Cell", "Royal"]
    def __init__ (self, score, visited):
        self.score = score
        self.visited = visited

    def visitedPlus(room):
        self.rooms[room] += 1
    def scoreAdded(newScore):
        self.score = self.score + newScore


class QAndA(object):
    def __init__(self, roomName, Q, answerList, pts, weight):
        self.roomName = roomName        #String
        self.Q = Q                      #string
        self.answerList = answerList    #list of strings
        self.pts = pts                  #int
        self.weight = weight            #int

class RoomQuestionList(object):
    # Defines a list of questions for a specific room.
    # We must call a loop on the addAQuestion method to add
    # all of the questions for this room.
    def __init__(self, roomName):
        self.roomName = roomName

    def addAQuestion(self):
        pass
        #code here to add a question to a room's stock list from a txt file

class Room(object):
	#Define what a room is, initializes variables for the instance of the object.
	#	Parameters needed (RoomName, Intro,  Doorlist)
	#	Defined functions of this class:
	#		PrintIntro(RoomName)
	#		printQuestions(RoomName, DoorList,)
 	#		PrintConclusion()
	#		PrintHelp(Topic)
	#		Improper(ImproperType)
    def __init__(self, roomName, intro, doorList, qSet):
		self.roomName = roomName  #string
		self.intro = intro        #string
		self.doorList = doorList  #List of strings
		self.qSet = qSet          #list each element is a QAndA object]
######################
###   End Classes  ###
######################

#################
### Functions ###
#################

## okay, I need a function here that will return all of a rooms traits,
## only knowing the name of the room. Lets call it roomAttributes(roomName)

def roomAttributes (roomName):
    if roomName == "Enter":
        doorList = ["Square", "Pentagram", "Circle"]
        qset = RoomQuestionList("Enter")
        for x in range (0, len(doorList)):
            qset.addAQuestion()
        return ["Enter",
        "This is the Entrance Room. You must solve riddles here",
        doorList,
        qset]
    elif roomNumber == "Pentagram":
        pass
    elif roomNumber == "Triangle":
        pass
    elif roomNumber == "Square":
        pass
    elif roomNumber == "Circle":
        pass
    elif roomNumber == "Star":
        pass
    elif roomNumber == "Dungeon":
        pass
    elif roomNumber == "Cell":
        pass
    else:
        pass

## enter_a_room ##
## Parameters needed: roomName string

def enter_a_room(roomName):
    atts = roomAttributes(roomName)
    room = Room(atts[0], atts[1], atts[2], atts[3])#need to pass in variables here.   #gets the info for this room.
    roomscore = 0                                   #reset roomscore
    print room.intro                                #print the intro
    print room.doorList                             #print the doorList
    questions = RoomQuestionList(roomName)          #get the question list
    numberOfQs = len(questions)                    # number of questions
    for door in doorList:                           #one question per door
        currentQ = random.randint(0, numberOfQs)    #choose a question
        roomscore += askrandomquestion(currentQ)    # assign the result of the
                                                #questioning to the roomscore
    thisGame.score += roomscore

    return nextRoom

def _main():
    """ This is the main program. It initializes
    uses only functions and classes previously
    defined."""
    play_a_game = True
    while play_a_game:
        score = 0                               #initial score
        visited = [0,0,0,0,0,0,0,0,0]           #times each room visited
        thisGame = Game(score, visited)         #initialize thisGame
        print "Game initialized and started."

        thisRoom = ""
        nextRoom = thisGame.rooms[0]
        while nextRoom != "Royal" and nextRoom != "Dungeon" and nextRoom != "Cell":
            nextRoom = enter_a_room(nextRoom)


        again = raw_input("Would you like to play again? Y or N >>")
        if again == "N":
            play_a_game = False
        elif again != "Y":
            print "LOL because you can't follow simple instructions, now you must play again!"
        else:
            pass
    print "Thanks for playing!"

_main()
