# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artits"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id bigserial PRIMARY KEY,
    timestamp numeric NOT NULL,
    user_id int NOT NULL,
    level varchar NOT NULL,
    song_id char(18),
    artist_id char(18),
    session_id int NOT NULL,
    location varchar NOT NULL,
    user_agent varchar NOT NULL,
    CONSTRAINT fk_users
        FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_songs
        FOREIGN KEY(song_id)
            REFERENCES songs(song_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_artists
        FOREIGN KEY(artist_id)
            REFERENCES artists(artist_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id int PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL, 
    gender char(1) NOT NULL,
    level varchar NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id char(18) PRIMARY KEY,
    title varchar NOT NULL,
    artist_id char(18) NOT NULL, 
    year int NOT NULL,
    duration float NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id char(18) PRIMARY KEY, 
    name varchar NOT NULL,
    latitude numeric,
    longitude numeric,
    location varchar NOT NULL
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    timestamp numeric PRIMARY KEY, 
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(timestamp, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
 INSERT INTO users(user_id, first_name, last_name, gender, level)
     VALUES (%s, %s, %s, %s, %s)
     ON CONFLICT (user_id) 
     DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, latitude, longitude, location)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (timestamp, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, songs.artist_id 
FROM songs JOIN artists ON artists.artist_id = songs.artist_id 
WHERE songs.title = %s
 AND  artists.name = %s
 AND  songs.duration = %s
""")



# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]