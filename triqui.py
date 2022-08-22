import main.py

def printIntro(introFile):
    
    '''
    Desarrollo de la lectura por medio de la funcion read gracias a que este 
    solo es necesario para lectura e impresion del mismo
    
    '''
    introFile = open('datos.txt')
    inputFile =  introFile.read()
    print(inputFile)
    inputFile.close()
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''
def drawBoard(board):
    # Esta función imprime el tablero en la consola
    
    # Argumentos:
    
    # Board: Lista de strings que representa el estado del tablero
    print (" ","|"," ","|"," ")
    print ("", "+","","+","_")
    print (" ","|"," ","|"," ")
    print ("", "+","","+","_")
    print (" ","|"," ","|"," ")

    # Desarrolle el cuerpo de la función aquí...

def inputPlayerLetter():
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".
    
    playerletter= input("Escoja el simbolo con el que desea jugar (X, O: ")
    while playerletter != "O" or playerletter != "X":
        print("La opcion ingresada es invalida, vuelva a intentar")
        playerletter= input("Escoja el simbolo con el que desea jugar (X, O: ")
    if playerletter=="X":
        computerletter="O"
    else:
        computerletter="X"
    letter=[playerletter, computerletter]    
    return letter

def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.
    first=random.randint(0,1)
    # Retorna el string "Usuario" si el usuario inicia el juego o
    if first==0:
        player="Usuario"
    else:
        player="Computadora"
    # el string "Computadora" si la computadora inicia el juego.
    # Desarrolle el cuerpo de la función aquí...
    return player
    
def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    board 
    letter
    move
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.
    move== 

    # Desarrolle el cuerpo de la función aquí...
    pass

def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    pass

def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    pass

def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    # Desarrolle el cuerpo de la función aquí...
    pass

def chooseRandomMoveFromList(board, movesList):
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    pass

def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    # 1. Verificar si la computadora puede ganar...

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...

    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...

    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...

    
continuar= false
FichasEnTablero
def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.
    while continuar:

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    continuar= True
    return continuar
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    
