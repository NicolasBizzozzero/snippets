public class Point3 {
    private int x;
    private int y;
    private int z;

    public Point3(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public void add(Point3 point) {
        x += point.getX();
        y += point.getY();
        z += point.getZ();
    }

    public boolean equals(Point3 point) {
        return (this.x == point.getX()) && (this.y == point.getY()) && (this.z == point.getZ());
    }

    public String toString() {
        return String.format("(%d, %d, %d)", x, y, z);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }
}