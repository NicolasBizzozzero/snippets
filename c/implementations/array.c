#include <malloc.h>
#include <stdio.h>
#define TRUE 1
#define FALSE 0

typedef struct ArrayInt {
	int size;
	int* array;
} ArrayInt;

void _print_warning_out_ouf_bound(int index, int array_size) {
	printf("WARNING: You're trying to access an element out of the bounds of the array.\nYour index: %d, Array size: %d\n", index, array_size);
}

void _print_warning_arraycreation_failed(void) {
	puts("WARNING: The memory allocation of the array failed. You're probably out of memory.\n");
}


ArrayInt* create_arrayint(const int array_size){
	ArrayInt* arrayInt = (ArrayInt*) malloc(sizeof(ArrayInt));
	arrayInt->size = array_size;
	arrayInt->array = (int*) malloc(array_size * sizeof(int));

	if (arrayInt == NULL || arrayInt->array == NULL)
		_print_warning_arraycreation_failed();

	return arrayInt;
}

void free_arrayint(ArrayInt* arrayInt){
	free(arrayInt->array);
	free(arrayInt);
}

void print_arrayint(ArrayInt* arrayInt){
	puts("[");

	int i;
	for (i=arrayInt->size-1; i > 0; i--){
		printf("%d, ", arrayInt->array[i]);
	}

	printf("%d]", arrayInt->array[++i]);
}


/**
 * Return 1 if index is out of bound of arrayInt, 0 otherwise.
 */
int is_out_of_bound(int index, ArrayInt* arrayInt) {
	if (index >= 0) {
		(index >= arrayInt->size) ? TRUE : FALSE;
	} else {
		(-index < arrayInt->size) ? TRUE : FALSE;
	}
}


/**
 * Return the element at the index 'index' of arrayInt.
 * If a negative number is passed as index, elements are
 * returned from the last element of the arrayInt.
 * Print a warning message if the index is out of bound, then return 
 */
int get(int index, ArrayInt* arrayInt) {
	if (is_out_of_bound(index, arrayInt) == TRUE) {
		_print_warning_out_ouf_bound(index, arrayInt->size);
	}

	if (index >= 0) {
		return arrayInt->array[index];
	} else {
		return arrayInt->array[index + arrayInt->size];
	}
}


/**
 * Return the address of an Arrayint deep-copied from arrayInt.
 */
ArrayInt* copy_arrayint(ArrayInt* arrayInt) {
	// Memory allocation of the copy
	ArrayInt* copy_arrayInt = (ArrayInt*) malloc(sizeof(ArrayInt));
	copy_arrayInt->size = arrayInt->size;
	copy_arrayInt->array = (int*) malloc(arrayInt->size * sizeof(int));
	if (copy_arrayInt == NULL || copy_arrayInt->array == NULL)
		_print_warning_arraycreation_failed();

	// Deep copy of the elements
	int i;
	for (i=arrayInt->size-1; i >= 0; i--){
		copy_arrayInt->array[i] = arrayInt->array[i];
	}

	return copy_arrayInt;
}


void append(int element, ArrayInt** arrayInt) {
	// Memory allocation of the copy
	ArrayInt* copy_arrayInt = (ArrayInt*) malloc(sizeof(ArrayInt));
	copy_arrayInt->size = arrayInt->size + 1;
	copy_arrayInt->array = (int*) malloc((arrayInt->size + 1) * sizeof(int));
	if (copy_arrayInt == NULL || copy_arrayInt->array == NULL)
		_print_warning_arraycreation_failed();

	// Deep copy of the elements
	int i;
	for (i=arrayInt->size-1; i >= 0; i--){
		copy_arrayInt->array[i] = arrayInt->array[i];
	}

	// Adding the last element
	copy_arrayInt->array[copy_arrayInt->size - 1] = element;

	// Deleting the previous array
	copy_arrayInt

}
void replace(int element, int index, ArrayInt* arrayInt) {

}


int pop(ArrayInt* arrayInt) {

}


int main(){
	ArrayInt* arrayInt = create_arrayint(6);
	arrayInt->array = {4, 8, 15, 16, 23, 42};
	print_arrayint(arrayInt);
	free_arrayint(arrayInt);

	return 0;
}
