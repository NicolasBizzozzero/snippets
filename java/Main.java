public class Main {
    public static void main(String args[]){
        int[] tab = {42, 8, 4, 23, 4, 16, 15, 42};


        System.out.println(stringMoiCa(tab));
        MesTris.insertion(tab, MesTris.Ordre.CROISSANT);
        System.out.println(stringMoiCa(tab));
    }

    public static String stringMoiCa(int[] tab){
        String s = "[";

        int i;
        for (i=0; i<tab.length-1; i++){
            s += String.format("%d, ", tab[i]);
        }
        s += String.format("%d]", tab[i]);

        return s;
    }
}