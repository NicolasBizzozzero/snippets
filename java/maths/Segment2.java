public class Segment2{
    private Point2 pointA;
    private Point2 pointB;

    public Segment2(Point2 pointA, Point2 pointB){
        this.pointA = pointA;
        this.pointB = pointB;
    }

    public int length(){
        return pointA.distance_from(pointB);
    }

    public int compareLengthWith(Segment2 otherSegment){
        return (this.length() - otherSegment.length());
    }

    public Point2 getPointA(){
        return pointA;
    }

    public Point2 getPointB(){
        return pointB;
    }

    public String toString(){
        return String.format("%s --- %s", pointA.toString(), pointB.toString());
    }

    public boolean equals(Segment2 otherSegment){
        return (pointA.equals(otherSegment.getPointA()) && pointB.equals(otherSegment.getPointB())) || (pointB.equals(otherSegment.getPointA()) && pointA.equals(otherSegment.getPointB()));
    }
}