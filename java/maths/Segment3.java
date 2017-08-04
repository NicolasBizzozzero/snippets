public class Segment3{
    private Point3 pointA;
    private Point3 pointB;

    public Segment3(Point3 pointA, Point3 pointB){
        this.pointA = pointA;
        this.pointB = pointB;
    }

    public int length(){
        return pointA.distance_from(pointB);
    }

    public int compareLengthWith(Segment3 otherSegment){
        return (this.length() - otherSegment.length());
    }

    public Point3 getPointA(){
        return pointA;
    }

    public Point3 getPointB(){
        return pointB;
    }

    public String toString(){
        return String.format("%s --- %s", pointA.toString(), pointB.toString());
    }

    public Segment2 toSegment2(){
        return new Segment2(pointA.toPoint2(), pointB.toPoint2());
    }

    public boolean equals(Segment3 otherSegment){
        return (pointA.equals(otherSegment.getPointA()) && pointB.equals(otherSegment.getPointB())) || (pointB.equals(otherSegment.getPointA()) && pointA.equals(otherSegment.getPointB()));
    }
}