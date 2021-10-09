# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id VARCHAR, start_time INTEGER, user_id VARCHAR, level VARCHAR, song_id VARCHAR, artist_id VARCHAR, session_id INTEGER, location VARCHAR, user_agent VARCHAR)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id VARCHAR, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_title VARCHAR, title VARCHAR, artist_id VARCHAR, year INTEGER, duration NUMERIC)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR, name VARCHAR, location VARCHAR, latitude NUMERIC, longitude NUMERIC)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time INTEGER, hour INTEGER, day INTEGER, week INTEGER, month INTEGER, year INTEGER, weekday VARCHAR)""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]