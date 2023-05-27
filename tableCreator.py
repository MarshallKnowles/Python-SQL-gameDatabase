# This Program Serves to create all of the tables we will be using within the python-SQL project.
#Due to scoping this file is just for development purposes.
import mysql.connector
setup( "a", "b", "c")
# Connect to server and database
def setup( hostname, username, password):

    print(hostname + ' ' + username +' ' + password )
    database = mysql.connector.connect(host= "localhost",user = "user", passwd = "userPass1!")
    myCursor = database.cursor()
    myCursor.execute("CREATE DATABASE IF NOT EXISTS game_data") 
    myCursor.execute("USE game_data")

    #Create all tables:
    myCursor.execute("CREATE TABLE IF NOT EXISTS players ( player_id INT AUTO_INCREMENT, name VARCHAR(20), level INT, PRIMARY KEY (player_id));")
    myCursor.execute("CREATE TABLE IF NOT EXISTS item_instances (instance_id INT AUTO_INCREMENT, item_id INT, player_id INT, durability INT, PRIMARY KEY(instance_id) );")
    myCursor.execute("CREATE TABLE IF NOT EXISTS items (item_id INT AUTO_INCREMENT, name VARCHAR(20), rarity VARCHAR(20), starting_durability INT, PRIMARY KEY(item_id));")
    #Foreign Key Assignment
    myCursor.execute("ALTER TABLE item_instances ADD FOREIGN KEY(item_id) REFERENCES items(item_id) ON DELETE CASCADE;")
    myCursor.execute("ALTER TABLE item_instances ADD FOREIGN KEY(player_id) REFERENCES players(player_id) ON DELETE CASCADE;")
    #OK THIS IS DONE!



