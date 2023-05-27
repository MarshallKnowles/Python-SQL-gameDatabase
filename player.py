#This function takes user input and adds a new row to the table
#necessary imports and declarations

import mysql.connector


def add( database, my_cursor ):
    new_player_name = "GREGGORIUS the infinite" #Greggorius
    while ( len(new_player_name) >= 20):
        new_player_name = str(input("Enter the name of your player (must be 20 characters or less): "))

    new_player_level = "bro is literally infinite idk what to say" #GREGGORIUS
    while (True):
        try:
            new_player_level = int(input("Enter the level of your player: "))
            break
        except:
            print("That is not a valid input try inputting an integer")

    #adding the new player
    my_cursor.execute("INSERT INTO players (name, level) VALUES( '" + new_player_name + " '," + str(new_player_level) +");")
    database.commit
    
def delete( database, my_cursor ):
    target_player_id = "Shmlonkius the weakened"
    while (True):
        try:
            target_player_id = int(input("Enter the player_id of the target player: "))
            break
        except:
            print("That is not a valid input try inputting an integer")
    my_cursor.execute("DELETE FROM players WHERE player_id= " + str(target_player_id) + ";")
    database.commit


def modify( database, my_cursor ):
    #1st level checks for player existence
    while(True):
        #2nd level checks for valid integer input
        while(True):
            try:
                player_id = int(input("Enter the ID number of target player: "))
                break
            except:
                print("That is not a valid input try inputting an integer")
        #Check if the player exists:
        my_cursor.execute("SELECT * FROM players WHERE player_id = " + str(player_id) +";")
        target_player = my_cursor.fetchone()
        print(target_player)
        if target_player is not None:
            print("Player found!")
            break
        else:
            print("That player does not exist. Try again")

    #Modify the player
    while(True):
        user_in = int(input("What would you like to modify? \n 1. The players name \n 2. The players level"))
        match user_in:
            case 1:
                new_player_name = "GREGGORIUS the infinite" #Greggorius

                while ( len( new_player_name ) >= 20):
                    new_player_name = str(input("Enter the new name of your player (must be 20 characters or less): "))
                
                my_cursor.execute("UPDATE players SET name = '"+ str(new_player_name) + "' WHERE player_id = " + str(player_id) +";")
                database.commit
                break
            case 2:
                new_player_level = "literally infinite idk what to say" #GREGGORIUS
                while (True):
                    try:
                        new_player_level = input("Enter the new level of your player: ")
                        break
                    except:
                        print("That is not a valid input try inputing an integer")

                my_cursor.execute("UPDATE players SET level = "+ str(new_player_level) + " WHERE player_id = " + str(player_id) +";")
                database.commit
                break

            case _:
                print("Invalid input please try inputing an integer")
            


def display( database, my_cursor ):
    my_cursor.execute("SELECT * FROM players;")
    print("player_id:           name:           level:")
    for ( player_id, name, level) in my_cursor:
        print( str(player_id) + "              " + name + "              " + str(level))

