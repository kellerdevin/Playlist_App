from db_operations import db_operations
from helper import helper

#use DB Operations class to create object to help us connect to database
db_ops = db_operations("./chinook.db")
data = helper.data_cleaner("songs.csv")

class search_by():

    def search_by_genre():
        #get all genres and allow user to choose one
        query = '''
        SELECT DISTINCT Genre
        FROM songs;
        '''

        print("Genres in playlist:")
        genres = db_ops.single_attribute(query)

        choices = {}
        for i in range(len(genres)):
            print(i,genres[i])
            choices[i] = genres[i]
        index = helper.get_choice(choices.keys())

        #how many records
        print("How many songs do you want returned for "+choices[index]+"?")
        print("Enter 1, 5, or 0 for all songs")
        num = helper.get_choice([1,5,0])

        #run query and show results
        query = "SELECT DISTINCT name FROM songs WHERE Genre =:genre ORDER BY RANDOM()"
        dictionary = {"genre":choices[index]}
        if num != 0:
            query +=" LIMIT:lim"
            dictionary["lim"] = num
        helper.pretty_print(db_ops.name_placeholder_query(query, dictionary))

    def search_by_feature():
    #give users features and return choice
        features = ['Danceability', 'Liveness', 'Loudness']
        choices = {}
        for i in range(len(features)):
            print(i, features[i])
            choices[i] = features[i]
        index = helper.get_choice(choices.keys())

        #how many records
        print("How many songs do you want returned for "+choices[index]+"?")
        print("Enter 1, 5, or 0 for all songs")
        num = helper.get_choice([1,5,0])

        print("Do you want results sorted in ASC or DESC?")
        order = input("ASC or DESC: ")

        #prepare query and show results
        query = "SELECT DISTINCT Name FROM songs ORDER BY "+choices[index]+" "+order
        dictionary = {}
        if num!=0:
            query += " LIMIT :lim"
            dictionary["lim"] = num
        helper.pretty_print(db_ops.name_placeholder_query(query,dictionary))

    
    def search_by_song_name(song_name):
        query = "SELECT * FROM songs WHERE name = '" + song_name + "'"
        db_ops.all_attributes(query)




