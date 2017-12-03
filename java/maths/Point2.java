public class Point2 {
    private int x;
    private int y;

    public Point2(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void add(Point2 point) {
        x += point.getX();
        y += point.getY();
    }

    public boolean equals(Point2 point2) {
        return (this.x == point2.getX()) && (this.y == point2.getY());
    }

    public String toString() {
        return String.format("(%d, %d)", x, y);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
