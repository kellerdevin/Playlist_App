from db_operations import db_operations

class user_choice():

    def get_user_update_choice(song_name, songID):
        user_choice = int(input("Update option: "))
        if user_choice == 1:
            new_name = None
            while(type(new_name) != str):
                new_name = input("Name to update to: ")
            query = "UPDATE songs SET Name = '" + new_name + "' WHERE songID = '" + songID +"'"
        elif user_choice == 2:
            new_artist = None
            while(type(new_artist) != str):
                new_artist = input("Artist to update to: ")
            query = "UPDATE songs SET Artist = '" + new_artist + "' WHERE songID = '" + songID +"'"
        elif user_choice == 3:
            new_album = None
            while(type(new_album) != str):
                new_album = input("Album to update to: ")
            query = "UPDATE songs SET Album = '" + new_album + "' WHERE songID = '" + songID +"'"
        elif user_choice == 4:
            new_release_date = None
            while(type(new_release_date) != str):
                new_release_date = input("Release Date to update to: ")
            query = "UPDATE songs SET releaseDate = '" + new_release_date + "' WHERE songID = '" + songID +"'"
        elif user_choice == 5:
            new_Explicit = None
            #while(type(new_Explicit) != bool):
            new_Explicit = input("Explicit (TRUE or FALSE): ")
            query = "UPDATE songs SET Explicit = '" + new_Explicit  + "' WHERE songID = '" + songID +"'"
        else:
            get_user_update_choice()
        return query