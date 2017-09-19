#include <stdio.h>
#include <stdlib.h>

#define BLACK "\x1B[30m"
#define RED "\x1B[31m"
#define GREEN "\x1B[32m"
#define YELLOW "\x1B[33m"
#define BLUE "\x1B[34m"
#define MAGENTA "\x1B[35m"
#define CYAN "\x1B[36m"
#define WHITE "\x1B[37m"
#define RESET "\x1B[0m"


/**
 * Writes a colored string to stdout up to but not including the NULL
 * character.
 * A newline character is appended to the output.
 */
int printc(char* color, const char* content);


int printc(char* color, const char* content) {
    return puts(color content RESET);
}

