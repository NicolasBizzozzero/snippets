import java.util.Arrays;

public class SizedFIFO {
    private int size;
    private Integer[] array;
    private int numberOfElements;

    public SizedFIFO(int size){
        this.size = size;
        this.array = new Integer[size];
        this.numberOfElements = 0;
    }

    public int getSize(){
        return size;
    }

    public int getNumberOfElements(){
        return numberOfElements;
    }

    public boolean add(Integer elementToAdd){
        if (numberOfElements >= size)
            return false;
        array[numberOfElements] = elementToAdd;
        numberOfElements++;
        return true;
    }

    public Integer pop(){
        if (numberOfElements <= 0)
            return null;

        Integer elementToReturn = array[0];
        shiftAllElementsToTheLeftOnce();
        numberOfElements--;
        return elementToReturn;
    }

    private void shiftAllElementsToTheLeftOnce(){
        int ceil = numberOfElements-1;
        int index = 1 ;
        while (index <= ceil){
            array[index-1] = array[index];
            index++;
        }
        array[ceil] = null;
    }

    public String toString(){
        if (size <= 0 || numberOfElements <= 0)
            return "[]";

        Integer[] reversedCopy = new Integer[numberOfElements];
        System.arraycopy(array, 0, reversedCopy, 0, numberOfElements);
        reverse(reversedCopy);
        return Arrays.toString(reversedCopy);
    }
}