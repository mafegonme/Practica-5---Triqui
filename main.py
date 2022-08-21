import triqui as tr

# 1. Mostrar mensaje de bienvenida
print ('Bienvenido al juego ')
print ('Main menu')
print ('1. Iniciar un nuevo juego ')
print ('2. Fin del juego ')
opcion= int(input("Escriba el numero de la opcion a la que desea acceder: ")
            
            
while opcion != 1 or opcion != 2:
    print("La opcion ingresada es invalida, vuelva a intentar")
    print ('Main menu')
    print ('1. Iniciar un nuevo juego ')
    print ('2. Fin del juego ')
    opcion= int(input("Escriba el numero de la opcion a la que desea acceder: ")

while opcion !=2:
    
    turn ="" # Indica quién tiene el turno para jugar, el usuario o la computadora.
    while True:
    
        # 2. Crear el tablero
        print (drawboard())
        # 3. El usuario debe seleccionar la marca
        # 4. Quién va primero el usuario o la computadora?
    
        print(turn + ' va primero.')
    
        jugando = True # El juego ha iniciado
    
        while jugando:
            if turn == 'Usuario': # 5. Turno del usuario
    
                # a. Mostrar tablero
                # b. Pedir jugada al usuario
                # c. Actualizar el tablero
    
                # d. Verificar si el usuario ha ganado el juego.
                #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
    
                # e. Verificar si hay empate.
                #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
    
                # f. Si el usuario no ha ganado y no hay empate, la computadora
                #    toma el siguiente turno
    
                turn = 'Computadora'
    
            else: # 6. Turno de la computadora.
    
                # a. Computadora hace jugada.
                # b. Actualizar el tablero.
    
                # c. Verificar si la computadora ha ganado el juego.
                #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
    
                # d. Verificar si hay empate.
                #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
    
                # f. Si la computadora no ha ganado y no hay empate, el usuario
                #    toma el siguiente turno.
    
                turn = 'Usuario'
    
        # 7. Preguntar si el usuario quiere jugar una vez mas
        print ('Main menu')
        print ('1. Iniciar un nuevo juego ')
        print ('2. Fin del juego ')
        opcion= int(input("Inserte el numero de la opcion que desea escoger: ")
                    
        while opcion != 1 or opcion != 2:
            print("La opcion ingresada es invalida, vuelva a intentar")
            print ('Main menu')
            print ('1. Iniciar un nuevo juego ')
            print ('2. Fin del juego ')
            opcion= int(input("Escriba el numero de la opcion a la que desea acceder: ")
        #    Si no, finalizar el programa.
    
    else: 
        print ("Game over, Fin del JUEGO")
    
