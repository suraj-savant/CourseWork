//Write a C/C++ program to illustrate the race condition.


#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
using namespace std;
void printchars(const char *str) {
    const char *ptr;
    int c;
    cout.setf(std::ios::unitbuf);  // Set the output to be unbuffered
    for (ptr = str; (c = *ptr++) != 0;) {
        putc(c, stdout);
    }
}

int main() {
    pid_t pid;
    for (int i = 0; i < 3; ++i) {
        if ((pid = fork()) < 0) {
           perror("fork error");
        } else if (pid == 0) {
            printchars("output from child\n");
            _exit(0);
        } else {
            printchars("output from parent\n");
        }
    }

    // Wait for all child processes to finish
    while (wait(nullptr) > 0);

    return 0;
}
