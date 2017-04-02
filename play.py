import pickle

from player import Player
from container import Container
from animal import Animal


class InitGame:
    animalContainer = None
    player = None
    
    
    def __init__(self):
        print 'Animal guessing game'

    def initContainer(self):
        self.animalContainer = Container()

    def addPlayer(self, player):
        self.player = player

    def getPlater(self):
        return self.player

    def getRootAnimal(self):
        # We need to add an animal by guessing
        if self.animalContainer.getRootNode() == None:
            self.animalContainer.initRoot()
        return self.animalContainer.getRootNode()

    def setRootAnimal(self, rootAnimal):
        self.animalContainer.setRootNode(rootAnimal)

    def loadGameData(self):
        try:
            gameFile = open('animals.dat', 'rb')
            self.animalContainer = pickle.load(gameFile)
            gameFile.close()
        except:
            print 'Creating new game data file'
            self.initContainer()
            self.animalContainer.initRoot()
            self.saveGame()

    def saveGame(self):
        gameFile = open('animals.dat', 'wb')
        pickle.dump(self.animalContainer,
                    gameFile,
                    pickle.HIGHEST_PROTOCOL)
        gameFile.close()

    def isPlayerAnswerOK(self, playerAnswer):
        if playerAnswer == 'J':
            return True
        elif playerAnswer == 'Y':
            return True
        elif playerAnswer == 'N':
            return True
        else:
            return False

    def showInfo(self):
        print '-------------------------------'
        print 'Answer questions with Y/N'
        print
        

#-------------------
# INIT GAME
#-------------------
player = Player()
game = InitGame()
game.loadGameData()
game.addPlayer(player)
animal = game.getRootAnimal()
inputOK = False

gameRunning = True
print 'Game running.'
while gameRunning:
    game.showInfo()
    playerAnswer = raw_input(animal.getQuestion()).upper()
    inputOK = game.isPlayerAnswerOK(playerAnswer)
    while not (inputOK):
        game.showInfo()
        playerAnswer = raw_input(animal.getQuestion()).upper()
        inputOK = game.isPlayerAnswerOK(playerAnswer)
        
    correctOrFalse = animal.isAnswerCorrect(playerAnswer)
    if correctOrFalse:
        print 'Bingo'
    else:
        print 'Bummer'
    gameRunning = False


#-------------------
# DONE
#-------------------
game.saveGame()
print 'Done'

