public abstract class ColorUtils{
	public static final int NOIR    = 0x000000;
	public static final int BLEU    = 0x0000FF;
	public static final int VERT    = 0x00FF00;
	public static final int CYAN    = 0x00FFFF;
	public static final int ROUGE   = 0xFF0000;
	public static final int MAGENTA = 0xFF00FF;
	public static final int JAUNE   = 0xFFFF00;
	public static final int BLANC   = 0xFFFFFF; 

	/*
	public static Paint getPaint(int argb){
		Paint paint = new Paint();
		paint.setColor(argb);
		return paint;
	}

	// TODO
	public static Paint getPaint(Color color){
		Paint paint = new Paint();
		paint.setColor(argb);
		return paint;
	}

	// TODO
	public static Paint getPeintureInverse(int argb){
		return 0xFFFFFFFF - argb;
	}

	// TODO
	public static Paint combiner(int argb1, int argb2){
		//return (argb1 + argb2)%0xFFFFFFFF;
		return argb1 + argb2;
	}*/
}