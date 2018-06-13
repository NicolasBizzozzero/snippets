/**
 * Source : http://ascii-table.com/ansi-escape-sequences.php
 *
 * These sequences define functions that change display graphics, control
 * cursor movement, and reassign keys.
 *
 * ANSI escape sequence is a sequence of ASCII characters, the first two of
 * which are the ASCII "Escape" character 27 (1Bh) and the left-bracket
 * character " [ " (5Bh). The character or characters following the escape
 * and left-bracket characters specify an alphanumeric code that controls a
 * keyboard or display function.
 *
 * ANSI escape sequences distinguish between uppercase and lowercase letters.
 *
 * Information is also available on :
 * http://ascii-table.com/ansi-escape-sequences-vt-100.php
 **/

/* Moves the cursor to the specified position (coordinates).
   If you do not specify a position, the cursor moves to the home position at
   the upper-left corner of the screen (line 0, column 0). This escape
   sequence works the same way as the following Cursor Position escape
   sequence. */
#define CURSOR_POSITION "\x1B[0;0H"
#define CURSOR_POSITION2 "\x1B[0;0f"

/* Moves the cursor up by the specified number of lines without changing
   columns. If the cursor is already on the top line, ANSI.SYS ignores this
   sequence. */
#define CURSOR_UP "\x1B[1A"

/* Moves the cursor down by the specified number of lines without changing
   columns. If the cursor is already on the bottom line, ANSI.SYS ignores this
   sequence. */
#define CURSOR_DOWN "\x1B[1B"

/* Moves the cursor forward by the specified number of columns without 
   hanging lines. If the cursor is already in the rightmost column, ANSI.SYS
   ignores this sequence. */
#define CURSOR_FORWARD "\x1B[1C"

/* Moves the cursor back by the specified number of columns without changing
   lines. If the cursor is already in the leftmost column, ANSI.SYS ignores
   this sequence. */
#define CURSOR_BACKWARD "\x1B[1D"

/* Saves the current cursor position. You can move the cursor to the saved
   cursor position by using the Restore Cursor Position sequence. */
#define SAVE_CURSOR_POSITION "\x1B[s"

/* Returns the cursor to the position stored by the Save Cursor Position
   sequence. */
#define RESTORE_CURSOR_POSITION "\x1B[u"

/* Clears the screen and moves the cursor to the home position (line 0, column
   0). */
#define ERASE_DISPLAY "\x1B[2J"

/* Clears all characters from the cursor position to the end of the line
   (including the character at the cursor position). */
#define ERASE_LINE "\x1B[K"

/* Set Graphics Mode:
   Esc[Value;...;Valuem
   Calls the graphics functions specified by the following values. These
   specified functions remain active until the next occurrence of this escape
   sequence. Graphics mode changes the colors and attributes of text (such as
   bold and underline) displayed on the screen. */
// Text attributes
#define ALL_ATTRIBUTES_OFF "\x1B[0m"
#define BOLD "\x1B[1m"
#define UNDERSCORE "\x1B[4m"
#define BLINK "\x1B[5m"
#define REVERSE_VIDEO "\x1B[7m"
#define CONCEALED "\x1B[8m"

// Foreground colors
#define BLACK_FOREGROUND "\x1B[30m"
#define RED_FOREGROUND "\x1B[31m"
#define GREEN_FOREGROUND "\x1B[32m"
#define YELLOW_FOREGROUND "\x1B[33m"
#define BLUE_FOREGROUND "\x1B[34m"
#define MAGENTA_FOREGROUND "\x1B[35m"
#define CYAN_FOREGROUND "\x1B[36m"
#define WHITE_FOREGROUND "\x1B[37m"

// Background colors
#define BLACK_BACKGROUND "\x1B[40m"
#define RED_BACKGROUND "\x1B[41m"
#define GREEN_BACKGROUND "\x1B[42m"
#define YELLOW_BACKGROUND "\x1B[43m"
#define BLUE_BACKGROUND "\x1B[44m"
#define MAGENTA_BACKGROUND "\x1B[45m"
#define CYAN_BACKGROUND "\x1B[46m"
#define WHITE_BACKGROUND "\x1B[47m"

/* Set Mode:
   Esc[=Valueh
   Changes the screen width or type to the mode specified by one of the
   following values. */
#define MONOCHROME_40_25 "\x1B[=0h"
#define COLOR_40_25 "\x1B[=1h"
#define MONOCHROME_80_25 "\x1B[=2h"
#define COLOR_80_25 "\x1B[=3h"
#define FOUR_COLORS_320_200 "\x1B[=4h"
#define MONOCHROME_320_200 "\x1B[=5h"
#define MONOCHROME_640_200 "\x1B[=6h"
#define LINE_WRAPPING "\x1B[=7h"
#define COLOR_320_200_GRAPHICS "\x1B[=13h"
#define COLOR_640_200 "\x1B[=14h"
#define MONOCHROME_640_350 "\x1B[=15h"
#define COLOR_640_350 "\x1B[=16h"
#define MONOCHROME_640_480 "\x1B[=17h"
#define COLOR_640_480 "\x1B[=18h"
#define COLOR_320_200_256_COLOR_GRAPHICS "\x1B[=19h"

/* Reset Mode:
   Esc[=Valuel
   Resets the mode by using the same values that Set Mode uses, except for 7,
   which disables line wrapping (the last character in this escape sequence is
   a lowercase L). */
#define RESET_MONOCHROME_40_25 "\x1B[=0l"
#define RESET_COLOR_40_25 "\x1B[=1l"
#define RESET_MONOCHROME_80_25 "\x1B[=2l"
#define RESET_COLOR_80_25 "\x1B[=3l"
#define RESET_FOUR_COLORS_320_200 "\x1B[=4l"
#define RESET_MONOCHROME_320_200 "\x1B[=5l"
#define RESET_MONOCHROME_640_200 "\x1B[=6l"
#define RESET_COLOR_320_200_GRAPHICS "\x1B[=13l"
#define RESET_COLOR_640_200 "\x1B[=14l"
#define RESET_MONOCHROME_640_350 "\x1B[=15l"
#define RESET_COLOR_640_350 "\x1B[=16l"
#define RESET_MONOCHROME_640_480 "\x1B[=17l"
#define RESET_COLOR_640_480 "\x1B[=18l"
#define RESET_COLOR_320_200_256_COLOR_GRAPHICS "\x1B[=19l"
