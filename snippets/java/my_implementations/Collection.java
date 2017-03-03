public abstract class Collection {
    protected int size;

    public int getSize(){
        return size;
    }


    /**
     * Return true if the collection is empty, false otherwise
     */
    public boolean isEmpty() {
        return (size == 0);
    }
}