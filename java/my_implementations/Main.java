public class Main {
    public static void main(String[] args) {
        Queue<Integer> maListe = new Queue<Integer>();
        System.out.println(maListe.toString());
        maListe.enqueue(4);
        System.out.println(maListe.toString());
        maListe.enqueue(8);
        System.out.println(maListe.toString());
        maListe.enqueue(15);
        System.out.println(maListe.toString());
        maListe.enqueue(16);
        System.out.println(maListe.toString());
        maListe.enqueue(23);
        System.out.println(maListe.toString());
        maListe.enqueue(42);
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
        System.out.println(maListe.toString());
        maListe.dequeue();
    }
}