public abstract class MaString {
	/**
	 * Remove the character at the index "index" of str
	 */
	public static String remove(String str, int index){
		return str.substring(0, index) + str.substring(index + 1);
	}


	/**
	 * Remove the character at the index "index" of str and replace it with "newString"
	 */
	public static String replace(String str, int index, String newString){
		return str.substring(0, index) +  newString + str.substring(index + 1);
	}


	/**
	 * Return the number of occurences of 'charToCount' inside string.
	 */
	public static int countOccurencesOfChar(String string, char charToCount){
		int index = string.length()-1;
		int occurences = 0;
		while (index >= 0) {
			if ((string.charAt(index)) == (charToCount))
				occurences++;
			index--;
		}
		return occurences;
	}


    /**
     * Return "str" but reversed.
     *
     * Example :
     * >>> print(reversed("Hello World !"));
     * "! dlroW olleH" 
     */
    public static String reversed(String str){
        char[] input = str.toCharArray();
        int begin = 0;
        int end = input.length - 1;
        char temp;
        while (end > begin){
            temp = input[begin];
            input[begin] = input[end];
            input[end] = temp;
            end--;
            begin++;
        }
        return new String(input);
    }
}