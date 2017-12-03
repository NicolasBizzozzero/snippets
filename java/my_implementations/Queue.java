/**
 * A Queue (or FIFO) is a collection of elements.
 */
public class Queue<E> extends Collection{
    private List<Object> list;


    public Queue() {
        list = new List<Object>();
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

        return list.get(0);
    }


    /**
     * Add element to the bottom of the Queue.
     */
    public void enqueue(E element) {
        list.append(element);
    }

    /**
     * Remove element to the top of the Queue.
     */
    public Object dequeue() {
        int size = list.getSize();
        if (size <= 0)
            return null;

        return list.remove(0);
    }


    public void rightRotate(int n){

    }

    public String toString(){
        return list.toString();
    }
}