import java.math.BigInteger;
import java.io.PrintWriter;
import java.util.Scanner;


public class Countable {
    private static final String EXTENSION_NAME = "ctbl";

    private BigInteger value;

    public Countable() {
        this.value = BigInteger.ZERO;
    }


    public Countable(String filepath) {
        load(filepath);
    }


    /**
     * Increment the Countable value by one.
     */
    public void increment() {
        value.add(BigInteger.ONE);
    }


    /**
     * Decrement the Countable value by one.
     */
    public void decrement() {
        value.subtract(BigInteger.ONE);
    }


    /**
     * Add The value 'toAdd' to the Countable value.
     */
    public void modify(BigInteger toAdd) {
        value.add(toAdd);
    }


    /**
     * Load the Countable from the file 'filepath'.
     * The filepath needs to end with the Countable extension name.
     * This method create and use its own Scanner.
     */
    public void load(String filepath) throws InvalidFileNameException {
        if (! asTheRightExtension(filepath)) {
            throw InvalidFileNameException(filepath);
        }

        Scanner scanner = new Scanner(createFile(filepath));
        this.value = BigInteger(scanner.useDelimiter("\\Z").next());
        scanner.close();
    }


    /**
     * Load the Countable from the file 'filepath'.
     * The filepath needs to end with the Countable extension name.
     */
    public void load(String filepath, Scanner scanner) throws InvalidFileNameException {
        if (! asTheRightExtension(filepath)) {
            throw InvalidFileNameException(filepath);
        }

        this.value = BigInteger(scanner.useDelimiter("\\Z").next());
    }


    /**
     * Dump the Countable value to the file 'filepath'.
     * The filepath needs to end with the Countable extension name.
     * This method create and use its own PrintWriter.
     */
    public void dump(String filepath) throws InvalidFileNameException {
        if (! asTheRightExtension(filepath)) {
            throw InvalidFileNameException(filepath);
        }

        File file = createFile(filepath);
        PrintWriter printWriter = new PrintWriter(file);
        printWriter.println(this.getValue());
        printWriter.close();
    }


    /**
     * Dump the Countable value to the file 'filepath'.
     * The filepath needs to end with the Countable extension name.
     */
    public void dump(String filepath, PrintWriter printWriter) throws InvalidFileNameException {
        if (! asTheRightExtension(filepath)) {
            throw InvalidFileNameException(filepath);
        }

        printWriter.println(this.getValue());
    }


    /**
     * Getter for the Countable value.
     */
    public String getValue() {
        return this.value.toString();
    }


    /**
     * Return 'true' if 'filepath' as the right extension (ends with the right
     * extension name), 'false' otherwise.
     */
    private boolean asTheRightExtension(String filepath) {
        return filepath.endsWith(String.format("%s%s", ".", EXTENSION_NAME));
    }


    /**
     * Create and return a File object whoes parents directories are created if
     * they doesn't exist.
     */
    private File createFile(String filepath) {
        File file = new File(filepath);

        // Create subdirectories if they doesn't exist already
        file.getParentFile().mkdirs();

        return file;
    }
}