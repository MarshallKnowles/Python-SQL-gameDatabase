#This function takes user input and adds a new row to the table
#necessary imports and declarations

import mysql.connector


def add( database, my_cursor ):
    #Prompts user for new player info and adds a new player to the database

    #User input and input checking
    new_player_name = "GREGGORIUS the infinite" #Greggorius
    while ( len(new_player_name) >= 20):
        new_player_name = str(input("\nEnter the name of your player (must be 20 characters or less):\n"))
    
    new_player_level = "bro is literally infinite idk what to say" #GREGGORIUS
    while (True):
        try:
            new_player_level = int(input("\nEnter the level of your player: \n"))
            break
        except:
            print("That is not a valid input try inputting an integer")

    #adding the new player
    my_cursor.execute("INSERT INTO players (name, level) VALUES( '" + new_player_name + " '," + str(new_player_level) +");")
    database.commit()
    print("Player: " + str(new_player_name) + " added!")

def delete( database, my_cursor ):
    #Prompts user for player id and deletes that player from the database

    #Collect user input
    target_player_id = "Shmlonkius the weakened"
    while (True):
        try:
            target_player_id = int(input("\nEnter the player_id of the target player:\n"))
            break
        except:
            print("That is not a valid input try inputting an integer")

    #Delete the player
    my_cursor.execute("DELETE FROM players WHERE player_id= " + str(target_player_id) + ";")
    database.commit()
    print("Player_id: " + str(target_player_id) + " deleted.")


def modify( database, my_cursor ):
    #Prompts user for player id and player modifications and applies them to the database

    #Prompt user for player_id
    #1st level checks for player existence
    while(True):
        #2nd level checks for valid integer input
        while(True):
            try:
                player_id = int(input("\nEnter the ID number of target player: \n"))
                break
            except:
                print("That is not a valid input try inputting an integer")
        #Check if the player exists:
        my_cursor.execute("SELECT * FROM players WHERE player_id = " + str(player_id) +";")
        target_player = my_cursor.fetchone()
        if target_player is not None:
            print("Player " + str(player_id) + " found!")
            break
        else:
            print("That player does not exist. Try again")

    #Modify the player
    while(True):
        user_in = int(input("\nWhat would you like to modify? \n 1. The players name \n 2. The players level\n"))
        match user_in:

            #Change Name
            case 1:
                new_player_name = str(input("\nEnter the new name of your player (must be 20 characters or less): \n"))

                while ( len( new_player_name ) >= 20):
                    new_player_name = str(input("Invalid name, the new name of your player must be 20 characters or less: "))
                
                my_cursor.execute("UPDATE players SET name = '"+ str(new_player_name) + "' WHERE player_id = " + str(player_id) +";")
                database.commit()
                print("Player_id: " + str(player_id) + " name updated to: " + new_player_name)
                break

            #Change Level
            case 2:
                new_player_level = "literally infinite idk what to say" #GREGGORIUS
                while (True):
                    try:
                        new_player_level = input("\nEnter the new level of your player:\n")
                        break
                    except:
                        print("That is not a valid input try inputing an integer")

                my_cursor.execute("UPDATE players SET level = "+ str(new_player_level) + " WHERE player_id = " + str(player_id) +";")
                database.commit()
                print("Player_id: " + str(player_id) + " level updated to: " + new_player_level)
                break

            case _:
                print("Invalid input please try inputing an integer")
            


def display( database, my_cursor ):
    my_cursor.execute("SELECT * FROM players;")
    print("\nplayer_id:          name:               level:")
    for ( player_id, name, level) in my_cursor:
        print( "%-*s%-*s%s" % (20,str(player_id),20,str(name), str(level) ) )

