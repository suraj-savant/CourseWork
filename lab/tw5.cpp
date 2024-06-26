

// Write a C/C++ program that creates a zombie and then calls system to execute the ps 
// command to Verify that the process is zombie
#include<iostream>
#include<stdlib.h>
#include<unistd.h>
#include <sys/wait.h>
int main(){
    pid_t pid;
    if ((pid=fork())<0){
       perror("fork error");
    }
    else if(pid==0){
        _exit(0);
    }
      sleep(4);
      system("ps -o pid,ppid,state,tty,command");
      _exit(0);
}
