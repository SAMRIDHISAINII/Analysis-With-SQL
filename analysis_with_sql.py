
import pandas as pd
import sqlite3

conn = sqlite3.connect('spotify.db')

data = pd.read_csv('spotify-2023.csv',encoding='latin-1')
data.to_sql('spotify', conn, if_exists='replace', index=False)
data.rename(columns={
    'artist(s)_name': 'artist_name',
    'danceability_%': 'danceability_percent',
    'valence_%': 'valence_percent',
    'energy_%': 'energy_percent',
    'acousticness_%': 'acousticness_percent',
    'instrumentalness_%': 'instrumentalness_percent',
    'liveness_%': 'liveness_percent',
    'speechiness_%': 'speechiness_percent'
}, inplace=True)

print(data)

query = "SELECT `artist(s)_name` AS artist_name, SUM(streams) AS total_streams FROM spotify GROUP BY `artist(s)_name` ORDER BY total_streams DESC;"
tables = pd.read_sql(query, conn)
tables

query2 = "Select released_year, COUNT(*) AS song_count from spotify group by released_year;"
tables2 = pd.read_sql(query2, conn)
tables2

query3 = "Select track_name, `artist(s)_name` AS artist_name, released_year, released_month, released_day From spotify Order By released_year DESC, released_month DESC, released_day DESC LIMIT 10;"
tables3 = pd.read_sql(query3, conn)
tables3

query4 = "Select track_name, `artist(s)_name` AS artist_name, in_spotify_charts AS spotify_rank, in_apple_charts AS apple_rank From spotify Order By released_year DESC, released_month DESC, released_day DESC LIMIT 10;"
tables4 = pd.read_sql(query4, conn)
tables4

query5 = "Select track_name, `artist(s)_name` AS artist_name, bpm From spotify where bpm > 150 order by bpm DESC LIMIT 10;"
tables5 = pd.read_sql(query5, conn)
tables5

query6 = "Select track_name, `artist(s)_name` AS artist_name, in_spotify_playlists AS spotify_playlists, in_apple_playlists AS apple_playlists From spotify order by in_spotify_playlists + in_apple_playlists DESC LIMIT 10;"
tables6 = pd.read_sql(query6, conn)
tables6

query7 = "SELECT track_name, `artist(s)_name` AS artist_name, `energy_%` as energy_percent FROM spotify WHERE `energy_%` > 80 ORDER BY `energy_%` DESC LIMIT 10;"
tables7 = pd.read_sql(query7, conn)
tables7

query8 = "SELECT track_name, `artist(s)_name` AS artist_name, `acousticness_%` as acousticness_percent FROM spotify WHERE `acousticness_%` < 10 ORDER BY `acousticness_%` DESC LIMIT 10;"
tables8 = pd.read_sql(query8, conn)
tables8

query9 = "SELECT track_name, `artist(s)_name` AS artist_name, `speechiness_%` as speechiness_percent FROM spotify WHERE `speechiness_%` > 10 ORDER BY `speechiness_%` DESC LIMIT 10;"
tables9 = pd.read_sql(query9, conn)
tables9

