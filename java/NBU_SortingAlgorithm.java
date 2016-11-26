public abstract class NBU_SortingAlgorithm {
	public enum Order {
		INCREASING,
		DECREASING
	}

	/**
	 * INSERTION SORT
	 * @author : BIZZOZZERO Nicolas
	 */
	public static void insertion(int[] array, Order order){
		int len = array.length;
		for (int i=1; i<len; i++){
			int key = array[i];
			
			// We put the key on the left of the array, in
			// the sorted subset of the array
			int j = i-1;
			while (j > 0 && array[j] > key){
				array[j+1] = array[j];
				j--;
			}
			array[j+1] = key;
		}
	}

	/**
     * Return a String representation of tab.
     */
    public static String arrayToString(int[] tab){
        String s = "[";
        int i;
        for (i=0; i<tab.length-1; i++){
            s += String.format("%d, ", tab[i]);
        }
        s += String.format("%d]", tab[i]);
        return s;
    }
}