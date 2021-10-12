# Purpose of sparkifydb
- A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
- In this project, we create database called sparkifydb and make analyzing what songs users are listening to possible.

# sparkifydb's schema design and ETL pipeline
## DB Schema
### Fact table

```
songplays
    songplay_id SERIAL
    start_time TIMESTAMP
    user_id VARCHAR
    level VARCHAR
    song_id VARCHAR
    artist_id VARCHAR
    session_id INT
    location TEXT
    user_agent TEXT
```

### Dimension table
```
users
    user_id INT
    first_name VARCHAR
    last_name VARCHAR
    gender CHAR(1)
    level VARCHAR
```

```
songs
    song_id VARCHAR
    title VARCHAR
    artist_id VARCHAR
    year INT
    duration FLOAT
```

```
artists
    artist_id VARCHAR
    name VARCHAR
    location TEXT
    latitude FLOAT
    longitude FLOAT
```

```
time
    start_time TIMESTAMP
    hour INT
    day INT
    week INT
    month INT
    year INT
    weekday VARCHAR
```

## ETL Pipeline
### etl.py
- this file plays role in etl pipline
- there are three functions in this file:
    - process_song_file
        - this function processes song related files(located in data/song _data)
    - process_log_file
        - this function processes log related files(located in data/log_data)
    - process_data
        - this function uses the two functions above and do etl jobs
### create_tables.py
- Create Fact and Dimension table 

### sql_queries.py
- This file contains helpful sql queries.