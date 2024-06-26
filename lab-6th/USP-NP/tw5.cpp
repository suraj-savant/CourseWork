#include<iostream>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(){
    pid_t pid;
    if((pid = fork()) < 0){
        perror("fork() error");
        return 1;
    }

    if(pid == 0){
        _exit(0);
        
    }

    sleep(4);
    system("ps -o pid,ppid,state,tty,command");
    _exit(0);
}