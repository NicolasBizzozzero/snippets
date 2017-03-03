#include "string.c"
#include <string.h>
#define __FILENAME_WIN__ (strrchr(__FILE__, '\\') ? strrchr(__FILE__, '\\') + 1 : __FILE__) // WINDOWS
#define __FILENAME_LIN__ (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__) // LINUX

enum OS = {WINDOWS, LINUX};

/**
 * Return the absolute path to the current directory
 */
char* get_current_directory(OS operating_system){
	// We get the absolute name of the current file
	char* current_directory = strdup(__BASE_FILE__);

	// We remove the name of the file
	if (operating_system == WINDOWS)
		remove_substring(current_directory, "\\dup_eraser.c");
	else if (operating_system == LINU)
		remove_substring(current_directory, "/dup_eraser.c");
	
	return current_directory;
}