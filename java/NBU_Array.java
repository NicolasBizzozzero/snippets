public abstract class NBU_Array {

    /**
     * Reversed arrayToReverse in-place.
     *
     * Example :
     * >>> array = {4, 8, 15, 16, 23, 42};
     * >>> print(Arrays.toString(array));
     * [4, 8, 15, 16, 23, 42]
     * >>> MyArrayClass.reverse(array);
     * >>> print(Arrays.toString(array));
     * [42, 23, 16, 15, 8, 4]
     */
    public static void reverse(Integer[] arrayToReverse){
        int ceil = arrayToReverse.length / 2;
        for (int i=0; i < ceil; i++){
                int temp = arrayToReverse[i];
                int index = arrayToReverse.length - i - 1;
                arrayToReverse[i] = arrayToReverse[index];
                arrayToReverse[index] = temp;
        }
    }

    public Static String toString(Object[] array){
        return Arrays.toString(array);
    }
}