from ChutesAndLadders.ChutesAndLadders import ChutesAndLadders
from TicTacToe.TicTacToe import TicTacToe

class BoardGames(object):

    #initialize game
    def __init__(self):
        myGameFactory = GameFactory()
        myGameFactory.registerGame(1, "TicTacToe")
        myGameFactory.registerGame(2, "ChutesAndLadders")

        choiceOutput = "Type the number of the game you would like to play or Q to Quit\n"
        for game in myGameFactory.GetGames:
            choice = str(game) + ") " + myGameFactory.GetGames[game] + "\n"
            choiceOutput += choice 
        choiceOutput += "Q) Quit\n" 

        validGame = False
        while(not(validGame)):
            game = input(choiceOutput)            

            if game == 'Q' or game == 'q':
                break
            elif (not(game.isdigit())):
                print("Choice is not a number")
            elif int(game) not in [1,2]:   
                print("Choice must be 1 or 2")   
            else:
                myGameFactory.getGame(int(game))

class GameFactory(object):
    def __init__(self):
        self.__games = {}

    @property
    def GetGames(self):
        return self.__games

    def registerGame(self, gameID, creator):
        self.__games[gameID] = creator

    def getGame(self, gameID):
        creator = self.__games[gameID]
        if not creator:
            raise Exception("Invalid gameID: {}".format(gameID))
        return eval(creator)()
        
if __name__ == '__main__':
    myGame = BoardGames()

