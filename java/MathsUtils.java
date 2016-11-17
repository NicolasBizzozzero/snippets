public abstract class MathsUtils{
	public class Point {
		private int x, y;

		public Point(int x, int y){
			this.x = x;
			this.y = y;
		}

		public String toString(){
			return String.format("(%d, %d)", x, y);
		}

		public boolean equals(Point p){
			return (x == p.getX()) && (y == p.getY() );
		}

		public void setX(int x){
			this.x = x;
		}

		public void setY(int y){
			this.y = y;
		}

		public int getX(){
			return x;
		}

		public int getY(){
			return y;
		}
	}
}