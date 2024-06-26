#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
using namespace std;

void printchars(const char *str)
{
    cout.setf(std::ios::unitbuf);
    while (*str != 0)
    {
        putc(*str++, stdout);
    }
}

int main()
{
    pid_t pid;
    for (int i = 0; i < 3; i++)
    {
        if ((pid = fork()) < 0)
        {
            perror("Fork errro");
            return 1;
        }
        else if (pid == 0)
        {
            // printchars("This is from child process\n");
            cout << "From the child\n";
            _exit(0);
        }
        else
        {
            // printchars("This is from the parent process\n");
            cout << "From the parent\n";
        }
    }

    while (wait(nullptr) > 0);

    return 0;
}
