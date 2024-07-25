from reproductor import ReproductorMusica, leer_canciones_desde_csv
from interfaz import InterfazReproductorMusica

if __name__ == "__main__":
    nombre_archivo = 'spotify_data.csv'
    reproductor = ReproductorMusica()
    leer_canciones_desde_csv(nombre_archivo, reproductor)

    interfaz = InterfazReproductorMusica(reproductor)
    interfaz.iniciar()
