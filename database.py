import sqlite3
import csv

drop_artist = '''DROP TABLE IF EXISTS artist'''
drop_album = '''DROP TABLE IF EXISTS album'''
drop_music = '''DROP TABLE IF EXISTS music'''
              
query_create_artist = ''' CREATE TABLE IF NOT EXISTS artist(
                                        artist_id integer primary key autoincrement,
                                        name text unique
); '''

query_create_album = ''' CREATE TABLE IF NOT EXISTS album(
                                        album_id integer primary key autoincrement,
                                        name text,
                                        album_release_date date,
                                        album_total_tracks integer,
                                        foreign key (artist_id) references artist(artist_id)
); '''

query_create:music = ''' CREATE TABLE IF NOT EXISTS music(
                                        music_id integer primary key,
                                        title text,
                                        tag text,
                                        duration integer,
                                        popularity integer,
                                        explicit integer,
                                        track_number,
                                        lyrics text,
                                        foreign key(album_id) references album(album_id)
); '''


conn = sqlite3.connect('spotify.sqlite')
cursor = conn.cursor()

cursor.execute(drop_artist)
cursor.execute(query_create_artist)

cursor.execute(drop_albumt)
cursor.execute(query_create_album)

cursor.execute(drop_music)
cursor.execute(query_create_music)

df = pd.read_csv('ds2_final.csv', encoding='latin-1', index_col = 0)

for index, record in df.iterrows():
    artist_name = record['artist']
    album_name = record['album_name']
    album_release_date = record['album_release_date']
    album_total_tracks = record['album_total_tracks']
    music_id = index
    title = record['title']
    tag = record['tag']
    duration = record['duration_ms']
    popularity = record['popularity']
    explicit record['explicit']
    track_number = record['track_number']
    lyrics = record['lyrics']
    
    cursor.execute('''INSERT INTO artist(name) VALUES(?)''', artist_name)
    conn.commit()
    
    album_artist = cursor.execute('''SELECT artist_id FROM artist where artist_name = ?''', artist_name)
    cursor.execute('''INSERT INTO album(album_name, album_release_date, album_total_tracks, artist_id) VALUES (?, ?, ?, ?)''', album_name, album_release_date, album_total_tracks, album_artist)    
    conn.commit()
    
    album_name = cursor.execute('''SELECT album_id FROM album where album_name = ?''', album_name)
    cursor.execute('''INSERT INTO music (music_id, title, tag, duration, popularity, explicit, track_number, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', music_id, title, tag, duration, popularity, explicit, track_number, lyrics)
    conn.commit()

