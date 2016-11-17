/*
 * This class is a very simple chronometer who can help you get
 * execution's time of a block of code. Here's a code example :
 */

/*
Timer timer = new Timer();
timer.start();
// Block code you want to mesure
timer.stop();
double time = getChronometredTime();
*/

/* Simply invoke reset() if you want to reset the timer.
 * 
 * This class can easily be broken, but I'm currently to lazy
 * to improve it.
 * TODO: Stop being lazy.
 */
public class Timer {
	private long beginning;
	private long end;

	public Timer(){

	}

	public void start(){
		beginning = System.nanoTime();
	}

	public void stop(){
		end = System.nanoTime();

		if (beginning == -1){
			// You pressed stop before having pressed start
		}
	}

	public void reset(){
		beginning = -1;
	}

	/**
	 * Protip : If this method return you -1, you fucked up something somewhere.
	 * This return the estimated chronometed time in second.
	 */
	public double getChronometredTime(){
		if (end == -1 || beginning == -1)
			return -1;

		return (end - beginning) / 1000000000.0;
	}
}