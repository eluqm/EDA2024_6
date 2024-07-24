import java.util.ArrayList;
import java.util.List;

public class Trie {
    private Node root;

    public Trie() {
        root = new Node();
    }

    public void agregarCancion(Cancion cancion) {
        String trackName = cancion.getTrackName().toLowerCase();
        Node current = root;

        for (char ch : trackName.toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) {
                current.children[index] = new Node();
            }
            current = current.children[index];
        }
        current.cancion = cancion;
    }

    public Cancion buscarCancion(String trackName) {
        Node current = root;
        for (char ch : trackName.toLowerCase().toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) {
                return null;
            }
            current = current.children[index];
        }
        return current.cancion;
    }

    public void eliminarCancion(String trackName) {
        eliminar(root, trackName.toLowerCase(), 0);
    }

    private boolean eliminar(Node current, String trackName, int depth) {
        if (current == null) {
            return false;
        }

        if (depth == trackName.length()) {
            if (current.cancion != null) {
                current.cancion = null;
                return true;
            }
            return false;
        }

        int index = trackName.charAt(depth) - 'a';
        boolean deleted = eliminar(current.children[index], trackName, depth + 1);

        if (deleted && current.children[index].cancion == null) {
            boolean hasChildren = false;
            for (int i = 0; i < 26; i++) {
                if (current.children[index].children[i] != null) {
                    hasChildren = true;
                    break;
                }
            }

            if (!hasChildren) {
                current.children[index] = null;
            }
        }

        return deleted;
    }

    public List<Cancion> obtenerTodasLasCanciones() {
        List<Cancion> canciones = new ArrayList<>();
        obtenerCanciones(root, canciones);
        return canciones;
    }

    private void obtenerCanciones(Node node, List<Cancion> canciones) {
        if (node == null) {
            return;
        }
        if (node.cancion != null) {
            canciones.add(node.cancion);
        }
        for (Node child : node.children) {
            obtenerCanciones(child, canciones);
        }
    }
}
