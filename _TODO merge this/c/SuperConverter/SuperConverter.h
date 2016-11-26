#define TRUE 1
#define FALSE 0

/* 
 * return 0 if the base_changement failed
 */
int base_changement(char *initialNumberString, int initialBase, int finalBase);

/* 
 * Transforme nombre de la forme 0b'00000000'
 * en 0x'00000000'
 */
int binary_to_hexadecimal(char *initialNumberString, int bits, int complementadeux);

int binary_to_decimal(char *initialNumber, int bits, int complementadeux);

int hexadecimal_to_binary(char *initialNumber, int bits, int complementadeux);

int hexadecimal_to_decimal(char *initialNumber, int bits);

int decimal_to_binary(char *initialNumber, int bits, int complementadeux);

int decimal_to_hexadecimal(char *initialNumber, int bits);

void GUI(void);

/*
 * Take a string and return the cast into integer of it.
 * return NULL if any of the character of the string isn't alphanumeric.
 */
int string_to_int(char *string);

/*
 * Take a character and return the cast into integer of it.
 * return NULL if the character isn't alphanumeric.
 */
int char_to_int(char character);

/*
 * Take an integer and return the cast into character of it.
 */
char int_to_char(int integer);

/*
 * Take an integer and return the cast into string of it.
 */
char* int_to_string(int integer);

/*
 * Return the number of power of ten in number.
 */
int floatlen(float number);