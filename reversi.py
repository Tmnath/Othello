from graphicalBoard import GraphicWindow
from threading import Thread
from queue import Queue
from array2d import Array2D
from random import randint

def askplayer(id):
    """
    DO NOT CHANGE THIS FUNCTION
    Ask for the nature of a player
    :param id: "rouge" or "bleu"
    :return:  'h' for a human player, 'I' for an IA player
    """
    res = ''
    while res != 'h' and res != 'I':
        res = input('Le joueur ' + str(id) + ' est-il (h)umain ou (I)A ? ')
        if res != 'h' and res != 'I':
            print('Il faut répondre h ou I, merci.')
    return res


def askstrategy():
    """
    DO NOT CHANGE THIS FUNCTION
    Ask for the IA strategy
    :return: 'b' for a basic strategy, 'a' for an advance strategy
    """
    res = ''
    while res != 'b' and res != 'a':
        res = input('L\'IA doit-elle utiliser une stratégie (b)asique ou (a)vancée ? ')
        if res != 'b' and res != 'a':
            print('Il faut répondre b ou a, merci.')
    return res


def fixparameters():
    """
    DO NOT CHANGE THIS FUNCTION
    fix the parameters
    :return: max pixels, number of rows, number of columns, playerone, playertwo, strategyone, strategytwo
    """
    nbmaxres = 1000
    nbrows = 8
    nbcols = 8
    playerone = askplayer('rouge')
    if playerone == 'I':
        strategyone = askstrategy()
    else:
        strategyone = ''
    playertwo = askplayer('bleu')
    if playertwo == 'I':
        strategytwo = askstrategy()
    else:
        strategytwo = ''

    return nbmaxres, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo


def run():
    """
    DO NOT CHANGE THIS FUNCTION
    Fix the size of the board, set the players, creates the graphical board, create the communication channel
     between the threads and launch the game
    :return: nothing
    """
    nbmaxres, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo = fixparameters()

    queue = Queue()

    gw = GraphicWindow(nbmaxres, nbrows, nbcols, queue)

    gamethread = Thread(target=game, args=(gw, queue, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo))
    gamethread.daemon = True
    gamethread.start()

    gw.draw()


def waitformouseclick(queue):
    """
    DO NOT CHANGE THIS FUNCTION
    Wait for a mouse click on the graphical board and return the coordinate
    :param queue: event queue
    :return: tuple (x, y) with x the line number and y the column number
    """
    return queue.get()

def coupsPossibles(): #Vérifie les coups possibles 
    coordPossibles = []
    

def game(gw, queue, nbrows, nbcols, playerone, playertwo, strategyone, strategytwo):
    """
    This is the entry function for the game. This the main function where you should start the project
    :param gw: la fenêtre graphique pour afficher
    :param queue: pour la communication entre les threads
    :param nbrows: nombre de lignes
    :param nbcols: nombre de colonnes
    :param playerone: 'h' si le premier joueur est humain, 'I' si c'est l'IA
    :param playertwo: 'h' si le second joueur est humain, 'I' si c'est l'IA
    :param strategyone: 'b' si l'IA une utilise une approche basique, 'a' si elle utilise une approche avancée
    :param strategyone: 'b' si l'IA deux  utilise une approche basique, 'a' si elle utilise une approche avancée
    :return: rien
    """
    
        
    
    
    gw.drawbluedisk(4, 3)
    gw.drawbluedisk(3, 4)
    gw.drawreddisk(3, 3)
    gw.drawreddisk(4, 4)
    
    

    print("Click on the board !")
    coord = waitformouseclick(queue)         #Stocke les coordonnées à l'endroit du clic
    gw.drawreddisk(coord[0], coord[1])
    
    
    #Drawing a redsquare on the click tile
    #gw.drawreddisk(coord[0], coord[1])
    

    ## Drawing a blue disk
    # gw.drawbluedisk(2, 2)

    ## Drawing a red disk
    # gw.drawreddisk(4, 6)

    ## Drawing a green square
    # gw.drawgreensquare(6, 2)

    ## Drawing a yellow square
    # gw.drawyellowsquare(7, 7)

    ## To "erase" from the graphical board you can draw a white square
    # gw.drawbluedisk(3, 3)
    # gw.drawwhitesquare(3, 3)

    ## Wait for a mouse click
    # print("Click on the board !")
    # coord = waitformouseclick(queue)
    # print("Click coordinate are : ", coord[0], coord[1])
    # Drawing a redsquare on the click tile
    # gw.drawreddisk(coord[0], coord[1])

    ## Wait for a mouse click
    # print("Click again !")
    # coord = waitformouseclick(queue)
    # print("Click coordinate are : ", coord[0], coord[1])
    # Drawing a redsquare on the click tile
    # gw.drawbluedisk(coord[0], coord[1])


# Start the game
# DO NOT CHANGE THIS INSTRUCTION
run()
