class Cancion:
    def __init__(self, artist_name, track_name, track_id, popularity, year, genre, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature):
        self.artist_name = artist_name
        self.track_name = track_name
        self.track_id = track_id
        self.popularity = popularity
        self.year = year
        self.genre = genre
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.time_signature = time_signature

    def __str__(self):
        return f"{self.artist_name} - {self.track_name} - {self.year}"
