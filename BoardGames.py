from ChutesAndLadders.ChutesAndLadders import ChutesAndLadders
from TicTacToe.TicTacToe import TicTacToe
from Othello.Othello import Othello

class BoardGames(object):

    # Display Game Menu with list of registered games
    @staticmethod
    def ShowGameMenu():
        choiceOutput = "Type the number of the game you would like to play or Q to Quit\n"
        for game in GameFactory.games:
            choice = str(game) + ") " + GameFactory.games[game] + "\n"
            choiceOutput += choice 
        choiceOutput += "Q) Quit\n" 

        validGame = False
        while(not(validGame)):
            game = input(choiceOutput)            

            if game == 'Q' or game == 'q':
                break
            elif (not(game.isdigit())):
                print("Choice is not a number")
            elif int(game) not in GameFactory.games:   
                print("Invalid choice")   
            else:
                GameFactory.getGame(int(game))

# Game Factory class for list of games to play
# Register the game in BoardGames class and add
# module import so that only className is needed
# when registering game now (also used on user menu)
class GameFactory(object):
    games = {}
    
    @classmethod
    def registerGame(cls, gameID, creator):
        cls.games[gameID] = creator

    @classmethod
    def getGame(cls, gameID):
        creator = cls.games[gameID]
        if not creator:
            raise Exception("Invalid gameID: {}".format(gameID))
        return eval(creator)()
        
if __name__ == '__main__':
    # Register list of games using className 
    GameFactory.registerGame(1, "TicTacToe")
    GameFactory.registerGame(2, "ChutesAndLadders")
    GameFactory.registerGame(3, "Othello")

    BoardGames.ShowGameMenu()

