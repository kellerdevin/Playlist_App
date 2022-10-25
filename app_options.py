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
        print_list.print_update_options()
        query = user_choice.get_user_update_choice(song_name, songID)
        db_ops.update_song(query)

    def delete_by_title():
        #find all of the song names on the playlist
        query = '''
        SELECT DISTINCT Name
        FROM songs;
        '''

        print("Song names in playlist: ")
        names = db_ops.single_attribute(query)

        #print songs to user and return their choice
        choices = {}
        for i in range(len(names)):
            print(i, names[i])
            choices[i] = names[i]
        index = helper.get_choice(choices.keys())

        selectedName = choices[index]

        #find songID of song with the selected name
        query = '''
        SELECT songID
        FROM songs
        WHERE Name = \'''' + selectedName + "\';"

        requestedID = db_ops.single_record(query)

        #print mathcing id
        print(requestedID)

        #Execute deletion
        query = "DELETE FROM songs WHERE songID = \'" + requestedID + "\';"
        db_ops.execute_query(query)

    #Finds all records with at least one NULL value and removes them
    def delete_nulls():

        #find all of the song names on the playlist
        query = '''
        SELECT songID
        FROM songs
        WHERE Name IS NULL OR
        Artist IS NULL OR
        Album IS NULL OR
        releaseDate IS NULL OR
        Genre IS NULL OR
        Explicit IS NULL OR
        Duration IS NULL OR
        Energy IS NULL OR
        Danceability IS NULL OR
        Acousticness IS NULL OR
        Liveness IS NULL OR
        Loudness IS NULL;
    '''

        songIDs = db_ops.single_attribute_none(query)

    #Prints all songIDs of records that contain a NULL value in any attribute
        for i in range(len(songIDs)):
            print(i, songIDs[i])

    #Execute deletion
        for songID in songIDs:
            query = "DELETE FROM songs WHERE songID = \'" + songID + "\';"
            db_ops.execute_query(query)



