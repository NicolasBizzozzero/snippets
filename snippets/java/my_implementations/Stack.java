/**
 * A Stack (or LIFO) is a collection of elements.
 */
public class Stack<E> extends Collection {
    private List<Object> list;


    public Stack() {
        list = new List<Object>();
    }


    /**
     * Return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return (this.size <= 0);
    }


    public void leftRotate(int n){

    }


    /**
     * Observe the top-most element without removing it.
     */
    public Object peek() {
        int size = list.getSize();
        if (size <= 0)
            return null;

        return list.get(size-1);
    }


    /**
     * Remove the top-most element of the stack.
     */
    public Object pop() {
        int size = list.getSize();
        if (size <= 0)
            return null;

        return list.remove(size-1);
    }


    /**
     * Add element to the top of the stack.
     */
    public void push(E element) {
        list.append(element);
    }


    public void rightRotate(int n){

    }


    public String toString(){
        return list.toString();
    }
}