#include <stdlib.h>


/**
 * Give the magnitude of error for a value and its approximation.
 */
double absolute_error(double value, double approximated_value) {
    return abs(value - approximated_value);
}


/**
 * Give the absolute error of a value and its approximation in terms of per
 * 100.
 */
double relative_error(double value, double approximated_value) {
    return (approximated_value - value) / value;
}
