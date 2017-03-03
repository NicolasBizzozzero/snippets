 #include <stdio.h>

/**
 * Swap the values located at the two adresses a and b.
 * This method uses a temporary variable.
 */
void swap(int* const a, int* const b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}


/**
 * Swap the values located at the two adresses a and b.
 * This method doesn't use a temporary variable.
 */
void add_swap(int* const a, int* const b){
	// If a and b are located at the same adress, their value will be set to 0
	if (a == b)
		return;

	*a = *a + *b;
	*b = *a - *b;
	*a = *a - *b;
}


/**
 * Swap the values located at the two adresses a and b.
 * This method doesn't use a temporary variable.
 */
void xor_swap(int* const a, int* const b){
	// If a and b are located at the same adress, their value will be set to 0
	if (a == b)
		return;

	*a = *a ^ *b;	// a = a XOR b
	*b = *b ^ *a;	// b = b XOR a
	*a = *a ^ *b;	// a = a XOR b
}


int main(int argc, char** argv){
	int a = 4;
	int b = 8;

	printf("Before swap    : %d, %d\n", a, b);
	swap(&a, &b);
	printf("After swap     : %d, %d\n", a, b);
	add_swap(&a, &b);
	printf("After ADD swap : %d, %d\n", a, b);
	xor_swap(&a, &b);
	printf("After XOR swap : %d, %d\n", a, b);

	return 0;
}