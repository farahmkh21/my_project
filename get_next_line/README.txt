# get_next_line
*his activity has been created as part of the 42 curriculum by fkhaldi*

##Description

This project implements the get_next_line function in C, which reads a file line by line.
The goal is to practice memory management, pointers, and file reading in C, while ensuring efficient handling of variable-length lines.
The function uses a static buffer to store leftover data between calls and works with any file descriptor.

##Instructions

Compile the project with all source files:

cc -Wall -Wextra -Werror main.c git_next_line.c -o gnl

Run the executable:

./gnl

The program reads the specified file line by line and prints each line to standard output.
Remember to free each line after use to prevent memory leaks.

##Resources

C Standard Library - stdlib.h
https://en.cppreference.com/w/c/memory

C Standard Library - unistd.h
https://pubs.opengroup.org/onlinepubs/9699919799/

Tutorial on reading files line by line in C
https://www.geeksforgeeks.org/c-program-read-file-line-line/

42 School get_next_line project instructions
https://github.com/42School/get_next_line

##AI Usage
AI assistance was used to review and correct code logic, fix segmentation faults, and optimize memory handling. Specifically, AI helped refactor utility functions, fix pointer misuse, and clarify the algorithm for reading lines efficiently.

##Algorithm Explanation

The function maintains a static buffer per file descriptor to keep leftover data from previous reads.

On each call, it checks for a newline character in the buffer.

If a newline exists, it extracts the line up to and including the newline and updates the buffer.

If not, it reads additional data from the file descriptor into the buffer and repeats the process.

When reaching the end of the file, any remaining data is returned as the last line.

This approach ensures:

Minimal system calls by reading in chunks (BUFFER_SIZE = 42)

Correct handling of lines of any length

Efficient memory usage with proper allocation and deallocation
