#include <math.h>
#include <stdio.h>
#define TRUE 1
#define FALSE 0

/* *
 * Return 1 if x is divisible by y, 0 otherwise.
 */
int is_divisible(int x, int y){
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
int abs(int n){
	if (n < 0){
		int tmp = n;
		n -= n;
		n -= tmp;
	}

	return n;
}