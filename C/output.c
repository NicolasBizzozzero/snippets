#include <stdio.h>
#include <stdlib.h>
#include "ansi_escape_sequences.h"


/**
 * Writes a colored string to stdout up to but not including the NULL
 * character.
 */
int printc(char* color, const char* content);


int printc(const char* color, const char* content) {
    return printf("%s%s%s", color, content, ALL_ATTRIBUTES_OFF);
}
