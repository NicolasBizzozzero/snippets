#include <math.h>
#include <stdio.h>
#include <stdarg.h>

#define TRUE 1
#define FALSE 0

/* *
 * Return 1 if x is divisible by y, 0 otherwise.
 */
int is_divisible_by(int x, int y){
	// The sign of x and y doesn't matter.
	// So to prevent modulo error, we take their absolute value.
	x = abs(x);
	y = abs(y);

	if (x < y || y == 0)
		return FALSE;
	return (x % y == 0)? TRUE : FALSE;
}

/* *
 * Return 1 if n is even, 0 otherwise.
 */
int is_even(int n){
	return (n % 2 == 0)? TRUE : FALSE;
}

/* *
 * Return 1 if n is odd, 0 otherwise.
 */
int is_odd(int n){
	return (n % 2 == 1)? TRUE : FALSE;
}

/* *
 * Return the last digit of n.
 */
int get_last_digit(int n){
	return abs(n % 10);
}

/* *
 * Return the digit at the place "digit index" of n.
 */
int get_digit(int n, int digit_index){
	
}

/* *
 * Return the sum of all digits of n.
 */
int sum_of_all_digits(int n){
	int sum = 0;
  	while (n != 0){
	    sum += n % 10;
	    n /= 10;
	}

  	return sum;
}

/* *
 * Return the number of digits in n.
 */
int len(int n){
	if (n == 0)
		return 1;

	int sum = 0;
	while (n != 0){
		sum++;
		n /= 10;
	}

	return sum;
}

/* *
 * Return the number n with his digits reversed
 */
int reverse(int n){
	int sum = 0;
	double k = pow(10, (len(n)-1));
	while (n != 0){
		sum += k * (n % 10);
		n /= 10;
		k /= 10;
	}

	return sum;
}

/* *
 * Return the number n multiplicated "times" times by 2
 */
int multiply_by_2(int n, unsigned int times){
	return n << times;
}

/* *
 * Return the number n divided "times" times by 2
 */
int divide_by_2(int n, unsigned int times){
	return n >> times;
}

/* *
 * Return n if n is greater than 0, -n otherwise.
 */
unsigned int absTODO_TEST(int n){
	if (n < 0) {
		int tmp = n;
		n -= n;
		n -= tmp;
	}
	return n;
}

unsigned int abs2TODO_TEST(int n){
	if (n < 0)
		return -n;
	return n;
}

/**
 * Return 1 if n is a prime number, 0 otherwise.
 * To optimize the program, we firstl check if n is even,
 * and iterate only with odd numbers until the square root of n.
 * We also store this square root on a variable, saving lot
 * of CPU's power because the formula is not
 * calculated for each iteration.
 */
char is_prime(unsigned int n){
    if (n <= 1 || (is_even(n) == TRUE && n != 2))
        return FALSE;
    
    unsigned int divisor = 3;
    double ceil = sqrt(n);
    while (divisor < ceil){
        if (is_divisible_by(n, divisor) == TRUE)
            return FALSE;
        divisor += 2;
    }
    return TRUE;
}

/**
 * Return the highest integer from all the integers passed by arguments.
 * The function can accept an infinite number of arguments, but you must pass
 * the number of arguments as the first parameter. If you pass the wrong number of arguments,
 * then the behaviour of the function is undefined.
 * ALL the arguments must be integers, otherwise the behaviour of the function is undefined.
 */
int max_int(const unsigned int number_of_arguments, ...){
        va_list arguments_list;
        va_start(arguments_list, number_of_arguments);

        register int i;
        int max, current_argument;

        max = va_arg(arguments_list, int);
        for(i = 1; i < number_of_arguments; i++) {
                if ((current_argument = va_arg(arguments_list, int)) > max)
                        max = current_argument;
        }

        va_end(arguments_list);
        return max;
}

/**
 * Return the lowest integer from all the integers passed by arguments.
 * The function can accept an infinite number of arguments, but you must pass
 * the number of arguments as the first parameter. If you pass the wrong number of arguments,
 * then the behaviour of the function is undefined.
 * ALL the arguments must be integers, otherwise the behaviour of the function is undefined.
 */
int min_int(const unsigned int number_of_arguments, ...){
        va_list arguments_list;
        va_start(arguments_list, number_of_arguments);

        register int i;
        int min, current_argument;

        min = va_arg(arguments_list, int);
        for(i = 1; i < number_of_arguments; i++) {
                if ((current_argument = va_arg(arguments_list, int)) < min)
                        min = current_argument;
        }

        va_end(arguments_list);
        return min;
}