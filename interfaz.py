import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar, Entry, Button
from reproductor import ReproductorMusica
class InterfazReproductorMusica:
    def __init__(self, reproductor):
        self.reproductor = reproductor
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Música")
        self.ventana.geometry("800x600")

        # Marco para las canciones disponibles
        self.frame_canciones = tk.Frame(self.ventana)
        self.frame_canciones.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.label_canciones = tk.Label(self.frame_canciones, text="Canciones", font=("Arial", 14))
        self.label_canciones.pack()

        self.search_frame = tk.Frame(self.frame_canciones)
        self.search_frame.pack(pady=5)

        self.label_buscar = tk.Label(self.search_frame, text="Buscar:")
        self.label_buscar.pack(side=tk.LEFT, padx=5)

        self.entry_buscar = Entry(self.search_frame)
        self.entry_buscar.pack(side=tk.LEFT, padx=5)

        self.boton_buscar = Button(self.search_frame, text="Buscar", command=self.buscar_canciones)
        self.boton_buscar.pack(side=tk.LEFT, padx=5)

        self.scrollbar_canciones = Scrollbar(self.frame_canciones)
        self.scrollbar_canciones.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_canciones = Listbox(self.frame_canciones, yscrollcommand=self.scrollbar_canciones.set, height=10)
        self.lista_canciones.pack(fill=tk.BOTH, expand=True)
        self.scrollbar_canciones.config(command=self.lista_canciones.yview)

        # Marco para la lista de reproducción y los botones de ordenamiento
        self.frame_playlist_ordenamiento = tk.Frame(self.ventana)
        self.frame_playlist_ordenamiento.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_playlist = tk.Frame(self.frame_playlist_ordenamiento)
        self.frame_playlist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_playlist = tk.Label(self.frame_playlist, text="Lista de reproducción", font=("Arial", 14))
        self.label_playlist.pack()

        self.scrollbar_playlist = Scrollbar(self.frame_playlist)
        self.scrollbar_playlist.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_playlist = Listbox(self.frame_playlist, yscrollcommand=self.scrollbar_playlist.set, height=10)
        self.lista_playlist.pack(fill=tk.BOTH, expand=True)
        self.scrollbar_playlist.config(command=self.lista_playlist.yview)

        self.frame_ordenamiento = tk.Frame(self.frame_playlist_ordenamiento)
        self.frame_ordenamiento.pack(side=tk.LEFT, padx=10)


def agregar_cancion(self):
        seleccion = self.lista_canciones.curselection()
        if seleccion:
            cancion = self.reproductor.obtener_canciones_disponibles()[seleccion[0]]
            self.reproductor.agregar_cancion(cancion)
            self.actualizar_playlist()
            messagebox.showinfo("Agregando ...", f"La Canción '{cancion.track_name}' fue añadida a la playlist.")
        else:
            messagebox.showerror("Error", "Seleccione una canción para agregar.")

