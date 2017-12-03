import java.lang.IndexOutOfBoundsException.*;

public class List<E> extends Collection {
    private Object array[];

    public List() {
        array = new Object[0];
    }

    /**
     * Add an element at the end of the list
     */
    public void append(E element) {
        extendArrayToTheRight(1);
        array[size-1] = element;
    }


    /**
     * Return the element at the index.
     */
    public Object get(int index) throws IndexOutOfBoundsException {
        if (!indexIsInBounds(index)) {
            throw new IndexOutOfBoundsException(String.format("Tried to access index %d of a List with a size of %d element(s).", index, size));
        }
        return array[index];
    }


    /**
     * Add an element a the beginning of the list.
     */
    public void prepend(E element) {
        extendArrayToTheLeft(1);
        array[0] = element;
    }


    /**
     * Remove and return the object at the index.
     */
    public Object remove(int index) throws IndexOutOfBoundsException{
        if (!indexIsInBounds(index)) {
            throw new IndexOutOfBoundsException(String.format("Tried to access index %d of a List with a size of %d element(s).", index, size));
        }

        Object objectToReturn = get(index);
        this.array = concatenateArrays(getSubArray(this.array, 0, index), getSubArray(this.array, index+1, size));
        this.size--;
        return objectToReturn;
    }


    /**
     * Return the index of the first occurence of element, or -1 if not found.
     */
    public int search(E element) {
        for (int index = 0; index < size; index++) {
            if (array[index].equals(element)){
                return index;
            }
        }
        return -1;
    }


    public String toString() {
        return java.util.Arrays.toString(array);
    }


    /**
     * Return a new array containing the content of leftArray concatenated with the content of rightarray.
     */
    private Object[] concatenateArrays(Object[] leftArray, Object[] rightArray) {
        int newSize = leftArray.length + rightArray.length;
        Object[] newArray = new Object[newSize];

        // Paste leftArray into newArray
        int newIndex;
        for (newIndex=0; newIndex < leftArray.length; newIndex++){
            newArray[newIndex] = leftArray[newIndex];
        }

        // Paste rightArray into newArray
        for (int i=0; i < rightArray.length; i++){
            newArray[newIndex] = rightArray[i];
            newIndex++;
        }

        return newArray;
    }


    /**
     * Add "elementsToAdd" null elements to the left of the array.
     */
    private void extendArrayToTheLeft(int elementsToAdd) {
        // Create a new array
        int newSize = size + elementsToAdd;
        Object newArray[] = new Object[newSize];

        // Copy the old array into the new array
        int indexNewArray = newSize-1;
        for (int indexOldArray = size-1; indexOldArray>=0; indexOldArray--) {
            newArray[indexNewArray] = array[indexOldArray];
            indexNewArray--;
        }

        array = newArray;
        size++;
    }

    /**
     * Add "elementsToAdd" null elements to the right of the array.
     */
    private void extendArrayToTheRight(int elementsToAdd) {
        // Create a new array
        int newSize = size+elementsToAdd;
        Object newArray[] = new Object[newSize];

        // Copy the old array into the new array
        int indexNewArray = newSize-elementsToAdd-1;
        for (int indexOldArray = size-1; indexOldArray>=0; indexOldArray--) {
            newArray[indexNewArray] = array[indexOldArray];
            indexNewArray--;
        }

        array = newArray;
        size++;
    }


    /**
     * Return the subarray from array[beginIndex, endIndex-1]
     */
    private Object[] getSubArray(Object[] array, int beginIndex, int endIndex) {
        Object[] newArray = new Object[endIndex - beginIndex];
        int indexNewArray = 0;
        for (int indexOldArray=beginIndex; indexOldArray < endIndex; indexOldArray++){
            newArray[indexNewArray] = array[indexOldArray];
            indexNewArray++;
        }
        return newArray;
    }


    /**
     * Return true if index is out of bounds, false otherwise?
     */
    private boolean indexIsInBounds(int index){
       return !(index < 0 || index >= size);
    }
}