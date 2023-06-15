
import mysql.connector
import user_in

#creates an item of item_id belonging to player
def create( database, my_cursor ):

    durability = 0
    #get item_id and make sure it exists
    while(True):
        target_item_id = user_in.get_int("\nPlease enter the id of the item you wish to create\n", "That is not an integer please try again")

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM items WHERE item_id = " + str(target_item_id) +";")
        target_item = my_cursor.fetchone()
        if target_item is not None:
            print("Item " + str(target_item_id) + " found!")
            durability = target_item[2]
            break
        else:
            print("That item does not exist please try again")

    #get the player_id and make sure it exists
    while(True):
        target_player_id = user_in.get_int("\nPlease enter the id of the player you would like the item to go to\n", "That is not an integer")

        #check if the player exists:
        my_cursor.execute("SELECT * FROM players WHERE player_id = "+ str(target_player_id) +";")
        target_player = my_cursor.fetchone()

        
        if target_player is not None:
            print("Player " +str(target_player_id) +" found!")
            break
        else:
            print("That player does not exist please try again")
    
    #Create the item instance
    my_cursor.execute("INSERT INTO item_instances (item_id, player_id, durability) VALUES( '" + str(target_item_id) + "', '" +str(target_player_id) + "', '" + str(durability) +"');")
    database.commit()
    print("REAL")



#deletes the selected instance
def delete( database, my_cursor ):
    #Prompts user for item id and deletes that item from the database


    #1st level checks for item existence
    while(True):
        #2nd level checks for valid integer input
        target_item_inst_id = user_in.get_int("\nEnter the ID number of target item instance: \n","That is not a valid input try inputting an integer" )

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM item_instances WHERE instance_id = " + str(target_item_inst_id) +";")
        target_inst = my_cursor.fetchone()
        if target_inst is not None:
            print("Item " + str(target_item_inst_id) + " found!")
            break
        else:
            print("That item does not exist. Try again")

    #Delete the item
    my_cursor.execute("DELETE FROM item_instances WHERE instance_id= " + str(target_item_inst_id) + ";")
    database.commit()
    print("Item_id: " + str(target_item_inst_id) + " deleted.")



#decrements the items durability by 1 and deletes item if durability goes to 0
def use(database, my_cursor):

    durability = 0
    #1st level checks for item existence
    while(True):
        #2nd level checks for valid integer input
        target_item_inst_id = user_in.get_int("\nEnter the ID number of target item instance: \n","That is not a valid input try inputting an integer" )

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM item_instances WHERE instance_id = " + str(target_item_inst_id) +";")
        target_inst = my_cursor.fetchone()
        if target_inst is not None:
            print("Item " + str(target_item_inst_id) + " found!")
            durability = target_inst[3]
            break
        else:
            print("That item does not exist. Try again")
    
    durability -= 1
    #decrement durabiltiy
    if(durability == 0):
        print("Target item has broken!")
        my_cursor.execute("DELETE FROM item_instances WHERE instance_id= " + str(target_item_inst_id) + ";")
        database.commit()
        print("Item_id: " + str(target_item_inst_id) + " deleted.")
    else:
        print("Used item")
        my_cursor.execute("UPDATE item_instances SET durability = " + str(durability) +" WHERE instance_id= " + str(target_item_inst_id) +";")
        database.commit()


#Displays all items_inst
def display( database, my_cursor ):
    my_cursor.execute("SELECT * FROM item_instances;")
    print("\ninstance_id:        item_id:            player_id:          durbility:")
    for ( instance_id, item_id, player_id, durability) in my_cursor:
        print( "%-*s%-*s%-*s%s" % (20,str(instance_id),20,str(item_id),20, str(player_id), str(durability) ) )

#Moves item from current player to player_id and checks if player_id is current one
def move(database, my_cursor):

    #1st level checks for item existance
    while(True):
        #2nd level checks for valid integer input
        instance_id = user_in.get_int("\nEnter the ID number of target item instance: \n","That is not a valid input try inputting an integer" )

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM item_instances WHERE instance_id = " + str(instance_id) +";")
        target_item = my_cursor.fetchone()
        if target_item is not None:
            print("Instance " + str(instance_id) + " found!")
            break
        else:
            print("That instance does not exist. Try again")

    #Get the player_id
    while(True):
        #2nd level checks for valid integer input
        player_id = user_in.get_int("\nEnter the ID number of the items new owner: \n","That is not a valid input try inputting an integer" )

        #Check if the item exists:
        my_cursor.execute("SELECT * FROM players WHERE player_id = " + str(player_id) +";")
        target_player = my_cursor.fetchone()
        if target_player is not None:
            print("Player " + str(player_id) + " found!")
            break
        else:
            print("That item does not exist. Try again")

    #transfer item
    my_cursor.execute("UPDATE item_instances SET player_id = " + str(player_id) + " WHERE instance_id = " + str(instance_id) +";")
    database.commit()
