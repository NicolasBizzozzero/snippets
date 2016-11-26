#include <stdio.h>
#include "SuperConverter.c"

int main(){
	char* number;
	char base;

	while(1){
		printf("Enter the number you want to convert :\n"
			   "> ");
		scanf("%s", number);

		printf("Enter the base you want your number to be displayed :\n"
			   "B/b : Binary\n"
			   "D/d : Decimal\n"
			   "H/h : Hexadecimal\n"
			   "> ");
		scanf("%s", &base);
	}

	return 0;
}