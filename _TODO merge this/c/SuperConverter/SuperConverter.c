#include <stdlib.h>
#include <math.h>
#include "SuperConverter.h"

/* 
 * return 0 if the base_changement failed
 */
int base_changement(char *initialNumberString, int initialBase, int finalBase){
	int initialNumberInteger = string_to_int(initialNumberString+2);

	if (initialNumberInteger == -1)
		return -1;

}

/* 
 * Transforme nombre de la forme 0b'00000000'
 * en 0x'00000000'
 */
int binary_to_hexadecimal(char *initialNumberString, int bits, int complementadeux){
	int initialNumberInteger = string_to_int(initialNumberString+2);

	if (initialNumberInteger == -1)
		return -1;
	
	int i;

	for (i=0; i < bits; i++){

	}

	initialNumberString[2] = 'x';
	return 1;
}

int binary_to_decimal(char *initialNumber, int bits, int complementadeux){

}

int hexadecimal_to_binary(char *initialNumber, int bits, int complementadeux){

}

int hexadecimal_to_decimal(char *initialNumber, int bits){

}

int decimal_to_binary(char *initialNumber, int bits, int complementadeux){

}

int decimal_to_hexadecimal(char *initialNumber, int bits){

}

void GUI(void){

}

/*
 * Take a string and return the cast into integer of it.
 * return NULL if any of the character of the string isn't alphanumeric.
 */
int string_to_int(char *string){
	int result = 0;
	int convertedInteger;
	int i;

	for (i =0; string[i] != '\0'; i++)
		convertedInteger = char_to_int(string[i]);

		if (convertedInteger == -1)
			return -1; 
		result += convertedInteger*(pow(10, i));

	return result;
}

/*
 * Take a character and return the cast into integer of it.
 * return NULL if the character isn't alphanumeric.
 */
int char_to_int(char character){
	if ('0' <= character <= '9')
		return (int) character;
	return -1;
}

/*
 * Take an integer and return the cast into character of it.
 */
char int_to_char(int integer){
	return (char) (integer + '0');
}

/*
 * Take an integer and return the cast into string of it.
 */
char* int_to_string(int integer){
	int i;
	char *string;

	for (i = floatlen(integer)-1; i != 0; i--)
		string[i] = int_to_char(integer%((int)pow(10, i)));

	return string;
}

/*
 * Return the number of power of ten in number.
 */
int floatlen(float number){
	int length = 0;

	while(number >= 1){
		number /= 10;
		length++;
	}

	return length;
}