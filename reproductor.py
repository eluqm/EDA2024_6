import csv
from models import Cancion
import random
class ReproductorMusica:
    def __init__(self):
        self.playlist = []
        self.canciones_disponibles = []
