#This function takes user input and adds a new row to the table
#necessary imports and declarations

import mysql.connector
import user_in

def add( database, my_cursor ):
    #Prompts user for new item info and adds a new item to the database

    #User input and input checking
    new_item_name = user_in.get_str_less("\nEnter the name of your item (must be 20 characters or less):\n", "\nInvalid input make sure your item's name is less than 20 characters\n", 20)

    new_item_rarity = user_in.get_int("\nEnter the rarity of your item:\n", "\nInvalid input make sure your item's rarity is entered as an integer.\n")

    new_item_starting_duability = user_in.get_int("\nEnter the starting durability of your item:\n", "\nInvalid input make sure your item's durability is entered as an integer.\n")
#adding the new item
    my_cursor.execute("INSERT INTO items (name, rarity,starting_durability) VALUES( '" + new_item_name + " '," + str(new_item_rarity) + " ," + str(new_item_starting_duability) + ");")
    database.commit()
    print("Item: " + str(new_item_name) + " added!")


def delete( database, my_cursor ):
    #Prompts user for item id and deletes that item from the database


    #1st level checks for item existence
    while(True):
        #2nd level checks for valid integer input
        target_item_id = user_in.get_int("\nEnter the ID number of target item: \n","That is not a valid input try inputting an integer" )

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM items WHERE item_id = " + str(target_item_id) +";")
        target_item = my_cursor.fetchone()
        if target_player is not None:
            print("Player " + str(target_item_id) + " found!")
            break
        else:
            print("That player does not exist. Try again")

    #Delete the player
    my_cursor.execute("DELETE FROM items WHERE item_id= " + str(target_item_id) + ";")
    database.commit()
    print("Item_id: " + str(target_item_id) + " deleted.")



def modify( database, my_cursor ):
    #Prompts user for player id and player modifications and applies them to the database

    #Prompt user for player_id
    #1st level checks for player existence
    while(True):
        #2nd level checks for valid integer input
        item_id = user_in.get_int("\nEnter the ID number of target item: \n","That is not a valid input try inputting an integer" )

        #Check if the player exists:
        my_cursor.execute("SELECT * FROM items WHERE item_id = " + str(player_id) +";")
        target_player = my_cursor.fetchone()
        if target_player is not None:
            print("Item " + str(player_id) + " found!")
            break
        else:
            print("That item does not exist. Try again")

    #Modify the player
    while(True):
        user_input = int(input("\nWhat would you like to modify? \n 1. The item's name \n 2. The item's rarity\n 3. The item's starting durability \n"))
        match user_input:

            #Change Name
            case 1:
                new_item_name = user_in.get_str_less("\nEnter the new name of the item (must be 20 characters or less): \n","Invalid name, the new name of the item must be 20 characters or less: ", 20 )
                my_cursor.execute("UPDATE items SET name = '"+ str(new_item_name) + "' WHERE item_id = " + str(item_id) +";")
                database.commit()
                print("Item_id: " + str(item_id) + " name updated to: " + new_item_name)
                break

            #Change Level
            case 2:
                new_item_rarity = user_int.get_int("\nEnter the new item rarity:\n","That is not a valid input try inputing an integer")
                my_cursor.execute("UPDATE items SET rarity = "+ str(new_item_rarity) + " WHERE item_id = " + str(item_id) +";")
                database.commit()
                print("Item_id: " + str(item_id) + " rarity updated to: " + new_item_rarity)
                break

            case _:
                print("Invalid input please try inputing an integer")
            


def display( database, my_cursor ):
    my_cursor.execute("SELECT * FROM items;")
    print("\nitem_id:          name:               rarity:             starting durbility:")
    for ( item_id, name, rarity, starting_durability) in my_cursor:
        print( "%-*s%-*s%-*s%s" % (20,str(item_id),20,str(name),20, str(rarity), str(starting_durability) ) )

