import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar, Entry, Button
from reproductor import ReproductorMusica
class InterfazReproductorMusica:
    def __init__(self, reproductor):
        self.reproductor = reproductor
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Música")
        self.ventana.geometry("800x600")

        # Espacio Canciones disponibles
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

        # Marco de la Lista de Reproducción y botones ordenar
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

        self.boton_ordenar_popularidad_asc = tk.Button(self.frame_ordenamiento, text="Popularidad Asc", command=lambda: self.ordenar_playlist('popularity'))
        self.boton_ordenar_popularidad_asc.pack(pady=2)

        self.boton_ordenar_popularidad_desc = tk.Button(self.frame_ordenamiento, text="Popularidad Desc", command=lambda: self.ordenar_playlist('popularity', True))
        self.boton_ordenar_popularidad_desc.pack(pady=2)

        self.boton_ordenar_ano_asc = tk.Button(self.frame_ordenamiento, text="Año Asc", command=lambda: self.ordenar_playlist('year'))
        self.boton_ordenar_ano_asc.pack(pady=2)

        self.boton_ordenar_ano_desc = tk.Button(self.frame_ordenamiento, text="Año Desc", command=lambda: self.ordenar_playlist('year', True))
        self.boton_ordenar_ano_desc.pack(pady=2)

        self.boton_ordenar_duracion_asc = tk.Button(self.frame_ordenamiento, text="Duración Asc", command=lambda: self.ordenar_playlist('duration_ms'))
        self.boton_ordenar_duracion_asc.pack(pady=2)

        self.boton_ordenar_duracion_desc = tk.Button(self.frame_ordenamiento, text="Duración Desc", command=lambda: self.ordenar_playlist('duration_ms', True))
        self.boton_ordenar_duracion_desc.pack(pady=2)

        # Botones Accion
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack(pady=10)

        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar", command=self.agregar_cancion)
        self.boton_agregar.pack(side=tk.LEFT, padx=5)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_cancion)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        self.boton_cambiar_orden = tk.Button(self.frame_botones, text="Cambiar Orden", command=self.cambiar_orden)
        self.boton_cambiar_orden.pack(side=tk.LEFT, padx=5)

        self.boton_reproduccion_aleatoria = tk.Button(self.frame_botones, text="Reproducción Aleatoria", command=self.reproduccion_aleatoria)
        self.boton_reproduccion_aleatoria.pack(side=tk.LEFT, padx=5)

        self.actualizar_lista_canciones()
        self.actualizar_playlist()

def agregar_cancion(self):
        seleccion = self.lista_canciones.curselection()
        if seleccion:
            cancion = self.reproductor.obtener_canciones_disponibles()[seleccion[0]]
            self.reproductor.agregar_cancion(cancion)
            self.actualizar_playlist()
            messagebox.showinfo("Agregando ...", f"La Canción '{cancion.track_name}' fue añadida a la playlist.")
        else:
            messagebox.showerror("Error", "Seleccione una canción para agregar.")
            
def eliminar_cancion(self):
        seleccion = self.lista_playlist.curselection()
        if seleccion:
            track_id = self.reproductor.obtener_playlist()[seleccion[0]].track_id
            self.reproductor.eliminar_cancion(track_id)
            self.actualizar_playlist()
            messagebox.showinfo("Eliminando ...", "Canción eliminada de la playlist.")
        else:
            messagebox.showerror("Error", "Seleccione una canción para eliminar.")
            
 def cambiar_orden(self):
        posicion_actual = simpledialog.askinteger("Cambiar Orden", "Ingrese la posición actual de la canción:")
        nueva_posicion = simpledialog.askinteger("Cambiar Orden", "Ingrese la nueva posición de la canción:")
        if posicion_actual is not None and nueva_posicion is not None:
            self.reproductor.cambiar_orden(posicion_actual-1, nueva_posicion-1)
            self.actualizar_playlist()

def reproduccion_aleatoria(self):
        self.reproductor.reproduccion_aleatoria()
        self.actualizar_playlist()

    def ordenar_playlist(self, key, reverse=False):
        self.reproductor.ordenar_playlist(key, reverse)
        self.actualizar_playlist()

 def buscar_canciones(self):
        filtro = self.entry_buscar.get().lower()
        canciones_filtradas = [cancion for cancion in self.reproductor.obtener_canciones_disponibles() if filtro in cancion.track_name.lower()]
        self.actualizar_lista_canciones(canciones_filtradas)

    def actualizar_lista_canciones(self, canciones=None):
        self.lista_canciones.delete(0, tk.END)
        if canciones is None:
            canciones = self.reproductor.obtener_canciones_disponibles()
        for cancion in canciones:
            self.lista_canciones.insert(tk.END, str(cancion))

    def actualizar_playlist(self):
        self.lista_playlist.delete(0, tk.END)
        for cancion in self.reproductor.obtener_playlist():
            self.lista_playlist.insert(tk.END, str(cancion))

    def iniciar(self):
        self.ventana.mainloop()
