from db_operations import db_operations
from helper import helper
from search_by import search_by
from print_list import print_list
from user_choice import user_choice

#use DB Operations class to create object to help us connect to database
db_ops = db_operations("./chinook.db")
data = helper.data_cleaner("songs.csv")

class app_options():

    def add_songs_into_db():
        print("Adding Songs")
        file_path =  input("Enter the file path of the new songs: ")
        if file_path != "":
            data = helper.data_cleaner(file_path)
            attribute_count = len(data[0])
            placeholders = ("?,"*attribute_count)[:-1]
            query = "INSERT INTO songs VALUES("+placeholders+")"
            db_ops.bulk_insert(query,data)
            print("Songs read")
        else:
            print("No new songs were added to the database")
    
    def update_song_info():
        print("Enter song name")
        song_name = input()
        songID = search_by.search_by_song_name(song_name)
        print(songID)
        print_list.print_update_options()
        query = user_choice.get_user_update_choice(song_name)
        db_ops.update_song(query)
        #Check if update value work
            #if true
                #update value
            #if false
                #print not gunna work
                #make them enter a new value

