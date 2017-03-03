public abstract class NBU_Math{
	public class Point2{
		private int x;
		private int y;

		public Point2(int x, int y){
			this.x = x;
			this.y = y;
		}

		public void add(Point2 point){
			x += point.getX();
			y += point.getY();
		}

	/*	public int distance_between(Point2 point){
			return sqrt();
		}*/

		public boolean equals(Point2 point2){
			return (this.x == point2.getX()) && (this.y == point2.getY());
		}

		public String toString(){
			return String.format("(%d, %d)", x, y);
		}

		public int getX(){
			return x;
		}

		public int getY(){
			return y;
		}
	}

	public class Point3{
		private int x;
		private int y;
		private int z;

		public Point3(int x, int y, int z){
			this.x = x;
			this.y = y;
			this.z = z;
		}

		public void add(Point3 point){
			x += point.getX();
			y += point.getY();
			z += point.getZ();
		}

	/*	public int distance_between(Point3 point){

		}*/

		public boolean equals(Point3 point3){
			return (this.x == point3.getX()) && (this.y == point3.getY()) && (this.z == point3.getZ());
		}

		public String toString(){
			return String.format("(%d, %d, %d)", x, y, z);
		}

		public int getX(){
			return x;
		}

		public int getY(){
			return y;
		}

		public int getZ(){
			return z;
		}
	}
}