#This is the main function and it will be the end executable.
#Does the following:
#1. Setup
#2. Runs CLI to query user for information
#setup
import mysql.connector, player_table_edit, items_table_edit, items_inst_table_edit


#Server setup and database access
print("Welcome to the game inventory database please make sure you have mySQL and the mySQL python connector installed.")
print("Please enter your mySQL server information here:")
pass_setup = False
while( not pass_setup ):
    hostname = input("Server Hostname: ")
    username = input("Username: ")
    password = input("Password: ")

    #Just setting the passwords automatically so I can test what I need to.
    hostname = "localhost"
    username = "user"
    password = "userPass1!"
    #sets up the tables in a try-catch
    try:
        #This FAT block generates all the tables and we need it here so everybody else can see database and my_cursor 
        print("Hostname: " +hostname + ', Username: ' + username +', Password: ' + password )
        database = mysql.connector.connect(host= str(hostname),user = "user", passwd = "userPass1!")
        my_cursor = database.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS gameData") 
        my_cursor.execute("USE gameData")

        #Create all tables:
        my_cursor.execute("CREATE TABLE IF NOT EXISTS players ( player_id INT AUTO_INCREMENT, name VARCHAR(20), level INT, PRIMARY KEY (player_id));")
        my_cursor.execute("CREATE TABLE IF NOT EXISTS item_instances (instance_id INT AUTO_INCREMENT, item_id INT, player_id INT, durability INT, PRIMARY KEY(instance_id) );")
        my_cursor.execute("CREATE TABLE IF NOT EXISTS items (item_id INT AUTO_INCREMENT, name VARCHAR(20), rarity VARCHAR(20), starting_durability INT, PRIMARY KEY(item_id));")
        #Foreign Key Assignment
        my_cursor.execute("ALTER TABLE item_instances ADD FOREIGN KEY(item_id) REFERENCES items(item_id) ON DELETE CASCADE;")
        my_cursor.execute("ALTER TABLE item_instances ADD FOREIGN KEY(player_id) REFERENCES players(player_id) ON DELETE CASCADE;")
        #OK THIS IS DONE!

    except: 
        print("There was an error please make sure the following are true: \n 1. You are entering the correct values for the server hostname, username, and password for your mySQL server. \n 2. Make sure that both Python and the mySQL python connector are installed. \n 3. Lastly please make sure that the mySQL connecter is within Pythons PATH variable.")
        print("Please try again:")
    else:
        print("Database sucessfully accessed!\n")
        pass_setup = True


#CLI TIME
while(True):
    user_select = input("Which group would you like to interract with?\n \n   1. Players \n   2. Items \n   3. Item Instances\n")
    match user_select:
        case '1':
            user_select = input("\nWhat would you like to do with the player table? \n   1. Add a new player \n   2. Remove a player \n   3. Modify a player in the table \n   4. Display the charactaristics of all players in the table\n")
            match user_select:
                case '1': 
                    player_table_edit.add( database, my_cursor )
                case '2':
                    player_table_edit.delete( database, my_cursor )
                case '3':
                    player_table_edit.modify( database,my_cursor )
                case '4':
                    player_table_edit.display( database, my_cursor )
                case _:
                    print("Invalid input")
        case '2': 
            user_select = input("\nWhat would you like to do with the items table? \n   1. Add a new item \n   2. Remove an item \n   3. Modify an item in the table \n   4. Display the charactaristics of all items in the table\n")
            match user_select:
                case '1': 
                    items_table_edit.add( database, my_cursor )
                case '2':
                    items_table_edit.delete( database, my_cursor )
                case '3':
                    items_table_edit.modify( database,my_cursor )
                case '4':
                    items_table_edit.display( database, my_cursor )
                case _:
                    print("Invalid input")
        case '3':
            user_select = input("\nWhat would you like to do with the item instance table? \n   1. Create a new item instance \n   2. Delete an item instance \n   3. Use an item instance \n   4. Display all item instances in the table\n   5. Move an item instance to a target players inventory \n")
            match user_select:
                case '1': 
                    items_inst_table_edit.create( database, my_cursor )
                case '2':
                    items_inst_table_edit.delete( database, my_cursor )
                case '3':
                    items_inst_table_edit.use( database,my_cursor )
                case '4':
                    items_inst_table_edit.display( database, my_cursor )
                case '5':
                    items_inst_table_edit.move( database, my_cursor)
                case _:
                    print("Invalid input")
        case _:
            print("This is an invalid input try again.")



