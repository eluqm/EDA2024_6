import csv
from models import Cancion
import random
class ReproductorMusica:
    def __init__(self):
        self.playlist = []
        self.canciones_disponibles = []
        
    def agregar_cancion(self, cancion):
        self.playlist.append(cancion)

    def eliminar_cancion(self, track_id):
        self.playlist = [cancion for cancion in self.playlist if cancion.track_id != track_id]

    def cambiar_orden(self, posicion_actual, nueva_posicion):
        if 0 <= posicion_actual < len(self.playlist) and 0 <= nueva_posicion < len(self.playlist):
            cancion = self.playlist.pop(posicion_actual)
            self.playlist.insert(nueva_posicion, cancion)

    def reproduccion_aleatoria(self):
        random.shuffle(self.playlist)

    def ordenar_playlist(self, key, reverse=False):
        self.playlist.sort(key=lambda cancion: getattr(cancion, key), reverse=reverse)

    def obtener_canciones_disponibles(self):
        return self.canciones_disponibles

    def obtener_playlist(self):
        return self.playlist
        
    def leer_canciones_desde_csv(nombre_archivo, reproductor):
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cancion = Cancion(
                row['artist_name'], row['track_name'], row['track_id'], row['popularity'], row['year'], row['genre'], 
                row['danceability'], row['energy'], row['key'], row['loudness'], row['mode'], row['speechiness'], 
                row['acousticness'], row['instrumentalness'], row['liveness'], row['valence'], row['tempo'], 
                row['duration_ms'], row['time_signature']
            )
            reproductor.canciones_disponibles.append(cancion)
