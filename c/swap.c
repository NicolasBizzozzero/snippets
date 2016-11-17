 #include <stdio.h>

void swap(int* a, int* b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void add_swap(int* a, int* b){
	// If a and b are located at the same adress, their value will be set to 0
	if (a == b)
		return;

	*a = *a + *b;
	*b = *a - *b;
	*a = *a - *b;
}

void xor_swap(int* a, int* b){
	// If a and b are located at the same adress, their value will be set to 0
	if (a == b)
		return;

	*a = *a ^ *b;	// a = a XOR b
	*b = *b ^ *a;	// b = b XOR a
	*a = *a ^ *b;	// a = a XOR b
}

int main(){
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