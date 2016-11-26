#ifndef PROJETS_MA_STRING_H
#define PROJETS_MA_STRING_H

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

#endif //PROJETS_MA_STRING_H
