public abstract class MesTris {
	public enum Ordre {
		CROISSANT,
		DECROISSANT
	}

	/**
	 * INSERTION SORT
	 * @author : BIZZOZZERO Nicolas
	 * 
	 */
	public static void insertion(int[] tab, Ordre ordre){
		int len = tab.length;

		for (int i=1; i<len; i++){
			int clef = tab[i];

			// On insère la clef dans l'ensemble trié du tableau, à gauche
			int j = i-1;
			while (j > 0 && tab[j] > clef){
				tab[j+1] = tab[j];
				j--;
			}

			tab[j+1] = clef;
		}
	}
}