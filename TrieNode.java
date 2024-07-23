public class Node {
    Cancion cancion;
    int altura;
    Node izquierda;
    Node derecha;

    public Node(Cancion cancion) {
        this.cancion = cancion;
        this.altura = 1;
    }
}
