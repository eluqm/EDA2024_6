import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class GestorListaReproduccion {
	private List<Cancion> playlist;
    private Trie trie;

    public GestorListaReproduccion() {
        playlist = new ArrayList<>();
        trie = new Trie();
    }

    // Método para agregar una canción a la lista de reproducción
    public void addSong(Cancion song) {
        playlist.add(song);
        trie.insert(song);
    } 
   // Método para eliminar una canción de la lista de reproducción
    public void removeSong(String trackName, String trackId) {
        Iterator<Cancion> iterator = playlist.iterator();
        while (iterator.hasNext()) {
        	Cancion song = iterator.next();
            if (song.getTrackName().equalsIgnoreCase(trackName) && song.toString().contains(trackId)) {
                iterator.remove();
                break;
            }
        }
        trie.delete(trackName, trackId);
    }
   // Método para cambiar el orden de las canciones en la lista
    public void changeOrder(int oldIndex, int newIndex) {
        if (oldIndex < 0 || oldIndex >= playlist.size() || newIndex < 0 || newIndex >= playlist.size()) {
            throw new IndexOutOfBoundsException("Índices fuera de rango");
        }
        Cancion song = playlist.remove(oldIndex);
        playlist.add(newIndex, song);
    }
   // Método para reproducir una canción de manera aleatoria
    public Cancion playRandom() {
        if (playlist.isEmpty()) {
            return null;
        }
        Random random = new Random();
        return playlist.get(random.nextInt(playlist.size()));
    }
   // Método para imprimir la lista de reproducción
    public void printPlaylist() {
        for (Cancion song : playlist) {
            System.out.println(song);
        }
    }   
   // Método para leer canciones desde un archivo CSV y agregarlas al trie
    public void readSongsFromCSV(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            br.readLine(); // Saltar la primera línea (encabezados)
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
// Manejar valores posibles nulos o vacíos y convertir a los tipos correctos
                String artistName = values[1];
                String trackName = values[2];
                String trackId = values[3]; // track_id no se convierte a número
                int popularity = parseIntSafe(values[4]);
                int year = parseIntSafe(values[5]);
                String genre = values[6];
                double danceability = parseDoubleSafe(values[7]);
                double energy = parseDoubleSafe(values[8]);
                int key = parseIntSafe(values[9]);
                double loudness = parseDoubleSafe(values[10]);
                int mode = parseIntSafe(values[11]);
                double speechiness = parseDoubleSafe(values[12]);
                double acousticness = parseDoubleSafe(values[13]);
                double instrumentalness = parseDoubleSafe(values[14]);
                double liveness = parseDoubleSafe(values[15]);
                double valence = parseDoubleSafe(values[16]);
                double tempo = parseDoubleSafe(values[17]);
                double durationMs = parseDoubleSafe(values[18]);
                int timeSignature = parseIntSafe(values[19]);

                Cancion song = new Cancion(artistName, trackName, trackId, popularity, year, genre, danceability,
                        energy, key, loudness, mode, speechiness, acousticness,
                        instrumentalness, liveness, valence, tempo, durationMs, timeSignature);
                addSong(song);
 }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
   // Método auxiliar para parsear enteros con manejo de excepciones
    private int parseIntSafe(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            return 0; // O puedes manejar el valor de error como desees
        }
    }

    // Método auxiliar para parsear doubles con manejo de excepciones
    private double parseDoubleSafe(String value) {
        try {
            return Double.parseDouble(value);
        } catch (NumberFormatException e) {
            return 0.0; // O puedes manejar el valor de error como desees
        }
    }
   // Método principal para probar el programa
    public static void main(String[] args) {
    	GestorListaReproduccion manager = new GestorListaReproduccion();

        // Leer canciones desde un archivo CSV
        String filePath = "E:/UNSA/EDA - Final/spotify_data.csv"; // Cambia esto por la ruta de tu archivo CSV
        manager.readSongsFromCSV(filePath);

        // Imprimimos la lista de reproducción
        System.out.println("Lista de reproducción:");
        manager.printPlaylist();

    }
}