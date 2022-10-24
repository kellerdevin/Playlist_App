# module defines operations to use with sqlite3 database
import sqlite3
from print_list import print_list


class db_operations():

    def __init__(self,conn_path): # constructor with connection path to db
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("connection made..")

    # function for bulk inserting records
    def bulk_insert(self,query,records):
        self.cursor.executemany(query,records)
        self.connection.commit()
        print("query executed..")

    # function to return a single value from table
    def single_record(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    # function to return a single attribute values from table
    def single_attribute(self,query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results

    #function to return all attribute values from table
    def all_attributes(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        songID = [i[0] for i in results]
        song_name = [i[1] for i in results]
        artist = [i[2] for i in results]
        album = [i[3] for i in results]
        release_date = [i[4] for i in results]
        explicit = [i[6] for i in results]
        print_list.print_changable_list(song_name[0],artist[0],album[0],release_date[0], explicit[0])
        return songID[0]
    # SELECT with named placeholders
    def name_placeholder_query(self,query,dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    def update_song(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def create_songs_table(self):
        query = '''
        CREATE TABLE songs(
            songID VARCHAR(22) NOT NULL PRIMARY KEY,
            Name VARCHAR(20),
            Artist VARCHAR(20),
            Album VARCHAR(20),
            releaseDate DATETIME,
            Genre VARCHAR(20),
            Explicit BOOLEAN,
            Duration DOUBLE,
            Energy DOUBLE,
            Danceability DOUBLE,
            Acousticness DOUBLE,
            Liveness DOUBLE,
            Loudness DOUBLE
        );
        '''

        self.cursor.execute(query)
        print('Table Created')

    # close connection
    def destructor(self):
        self.connection.close()
