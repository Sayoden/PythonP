#!/usr/bin/python3

import os
import termios
import threading
import time

######################################################################################
# Constantes et variables globales
######################################################################################

FOND = '\x1b[6;30;42m'
ENDC = '\x1b[0m'

QUIT = 5
LEFT = 1
RIGHT = 2
DOWN = 3
UP = 4
keylist = {'q' : QUIT,'\x1b[A' : UP, '\x1b[B' : DOWN, '\x1b[C' : RIGHT, '\x1b[D' : LEFT,}


VIDE = 0
OBJET = 1
SNAKE = 2
NBLIGNE = 20
NBCOLONNE = 60

# Question 1 :
board = []
speed = 0.1
score = 0
exitFlag = 0
mouv = (1, 0)

# Question 2 :
snakePos = [(0, 0)]

term = open("/dev/tty", "r")

######################################################################################
# Fonctions
######################################################################################

def getkey():
    global term
    
    fd = term.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = ''
    try:        
        c = (os.read(fd, 1)).decode()
        if(c == '\x1b'):
            c += (os.read(fd, 1)).decode()
            c += (os.read(fd, 1)).decode()
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return c

def get():    
    k = getkey()
    print(k)
    if k == '':
        return 0
    if k in keylist:
        return keylist.get(k)

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        collectMouvement(self)
        print ("Exiting " + self.name)

def collectMouvement(threadName):
    global exitFlag
    global mouv
    
    while exitFlag == 0:                    
        k = get()
        print(k)
        if k == QUIT:
            exitFlag = 1
        elif k == LEFT:
            mouv = (0, -1)
        elif k == RIGHT:
            mouv = (0, 1)
        elif k == UP:
            mouv = (-1, 0)
        elif k == DOWN:
            mouv = (1, 0)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fonctions pour le jeu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def createBoard(nbLigne : int, nbColonne : int):
    """
    Retourne un tableau (une liste de liste) initialisé avec des zéros
    Cette fonction prend en paramètre deux entiers :
       - nbLigne   : le nombre de lignes du tableau
       - nbColonne : le nombre de colonnes du tableau
    La fonction retourne une liste de liste. 
    """
    tab = []
    for i in range(nbLigne):
        L = []
        for j in range(nbColonne):
            L.append(0)
        tab.append(L)
    return tab


def printBoard(board, score):
    """
    Afficher le plateau.
    Cette fonction prend en paramètre une liste de liste
        - board   : le plateau du jeu
    """
    for i in range(board):
        for j in range(len(i)):
            print("*")

    
def putSeed(board):
    """
    Place un objet de manière aléatoire dans le tableau à un endroit libre.
    Cette fonction prend en paramètre une liste de liste
        - board   : le plateau du jeu   

    La fonction retourne la position de l'objet ou un tuple vide si il
    n'y a pas d'emplacement libre (la partie est terminée)    
    """


def deplace(board, snakePos, mouv):
    """
    Déplace le serpent.
    Cette fonction prend en paramètre :
        - board, le plateau du jeu
        - snake, la position du serpent dans le jeu
        - mouv, une direction
    Cette fonction retourne True si le déplacement est possible, False sinon
    """


def hitObject(snake, obj):
    """
    Cette fonction retourn vrai si le serpent a heurté l'objet 
    """

    
########################################################################################
# Programme principal
########################################################################################


# Create and start the thread listener
thread1 = myThread(1, "Keyboard listener", 1)
thread1.start()

# Create the board
board = createBoard(NBLIGNE, NBCOLONNE)
board[snakePos[0][0]][snakePos[0][1]] = SNAKE
obj = putSeed(board)
printBoard(board, score)
    
while(exitFlag == 0):
    time.sleep(speed)
    if deplace(board, snakePos, mouv):
        printBoard(board, score)
    else:
        print("You lose: press key")
        exitFlag = 1

    if(hitObject(snakePos, obj)):
        obj = putSeed(board)
        score += 1

term.close()
thread1.join()
os.system("reset")
print ("Exiting Main Thread")
