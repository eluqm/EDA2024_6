public class Cancion {
    private String artist_name;
    private String track_name;
    private String track_id;
    private int popularity;
    private int year;
    private String genre;
    private double danceability;
    private double energy;
    private int key;
    private double loudness;
    private int mode;
    private double speechiness;
    private double acousticness;
    private double instrumentalness;
    private double liveness;
    private double valence;
    private double tempo;
    private double duration_ms;
    private int time_signature;

    // Constructor y getters

    public Cancion(String artist_name, String track_name, String track_id, int popularity, int year, String genre, double danceability, double energy, int key, double loudness, int mode, double speechiness, double acousticness, double instrumentalness, double liveness, double valence, double tempo, double duration_ms, int time_signature) {
        this.artist_name = artist_name;
        this.track_name = track_name;
        this.track_id = track_id;
        this.popularity = popularity;
        this.year = year;
        this.genre = genre;
        this.danceability = danceability;
        this.energy = energy;
        this.key = key;
        this.loudness = loudness;
        this.mode = mode;
        this.speechiness = speechiness;
        this.acousticness = acousticness;
        this.instrumentalness = instrumentalness;
        this.liveness = liveness;
        this.valence = valence;
        this.tempo = tempo;
        this.duration_ms = duration_ms;
        this.time_signature = time_signature;
    }
    
    // Getters:

       public String getArtistName() {
        return artist_name;
    }

    public String getTrackName() {
        return track_name;
    }

    public String getTrackId() {
        return track_id;
    }

    public int getPopularity() {
        return popularity;
    }

    public int getYear() {
        return year;
    }

    public String getGenre() {
        return genre;
    }

    public double getDanceability() {
        return danceability;
    }

    public double getEnergy() {
        return energy;
    }
   public int getKey() {
        return key;
    }

    public double getLoudness() {
        return loudness;
    }

    public int getMode() {
        return mode;
    }

    public double getSpeechiness() {
        return speechiness;
    }

    public double getAcousticness() {
        return acousticness;
    }

    public double getInstrumentalness() {
        return instrumentalness;
    }

    public double getLiveness() {
        return liveness;
    }

    public double getValence() {
        return valence;
    }

    public double getTempo() {
        return tempo;
    }

    public double getDurationMs() {
        return duration_ms;
    }

    public int getTimeSignature() {
        return time_signature;
    }
}
