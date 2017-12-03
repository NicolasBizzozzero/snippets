.data

.text

.globl main
	# Return the sum of all integers located at the array which start at `$16`.
	main:
		ori $16, $0, 0
		ori $17, $0, 10

	while:
		addiu $16, $16, 1
		beq $16, $17, endwhile
		j while

	endwhile:
		ori $2, $0, 10
		syscall
