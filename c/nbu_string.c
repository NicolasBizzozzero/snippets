#include <windef.h>
#include <malloc.h>
#include "nbu_string.h"

/**
 * Return the number in str.
 */
unsigned int len(char* str);

/**
 * Create and return a copy of str.
 */
char* copy(char* str);

/**
 * Return a reversed copy of str
 */
char* reverse(char* str);

/**
 * Return the number of time c appear in str.
 */
unsigned int count(char* str, char c);

/**
 * Return the number of time substr appear in str.
 */
unsigned int count_substr(char* str, char* substr);

void str_free(char* str);


unsigned int len(char* str) {
    if (str == NULL)
        return 0;

    unsigned int len = 0;
    while (*str != '\0'){
        len++;
        str++;
    }
    return len;
}

/*char* copy(char* str){
    if (str == NULL)
        return NULL;

    // Allocate memory
    char* copy = (char*) malloc(len(str)*sizeof(char)+1); // We need to add 1 byte for the '\0' character.

    // Duplication of the string
    char* p_copy = copy;
    while (*str != '\0'){
        *p_copy = *str;
        p_copy++;
        str++;
    }

    return copy;
}*/
char* copy(char* str){
    if (str == NULL)
        return NULL;

    // Allocate memory
    char[] copy = char[len(str)];

    // Duplication of the string
    char* p_copy = copy;
    while (*str != '\0'){
        *p_copy = *str;
        p_copy++;
        str++;
    }

    return copy;
}

unsigned int count(char *str, char c) {
    if (str == NULL)
        return 0;

    unsigned int counter = 0;
    while (*str != '\0'){
        if (*str == c)
            counter++;

        str++;
    }
    return counter;
}

unsigned int count_substr(char *str, char *substr) {
    if (str == NULL || substr == NULL || substr == "\0")
        return 0;

    unsigned int counter = 0;
    char* substr_copy = substr;
    while (*str != '\0'){


        str++;
    }
    return counter;
}

char *reverse(char *str) {
    if (str == NULL)
        return NULL;

    unsigned int len_original_str = len(str);

    // Allocate memory
    char* reversed_str = (char*) malloc(len_original_str*sizeof(char)+1); // We need to add 1 byte for the '\0' character.

    // Creating the reversed string
    char* p_reversed_str = reversed_str;
    str += len_original_str-1;
    int i;
    for (i=0; i < len_original_str; i++){
        *p_reversed_str = *str;
        p_reversed_str++;
        str--;
    }

    return reversed_str;
}

void str_free(char* str){
    if (str == NULL)
        return;

    free(str);
}

void remove_substring(char* s, const char* toremove){
	while((s = strstr(s, toremove)))
		memmove(s, s+strlen(toremove), 1 + strlen(s + strlen(toremove)));
}
