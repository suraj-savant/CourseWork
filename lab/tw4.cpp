#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <filename>" << endl;
        return 1;
    }

    char temp[1000];
    setbuf(stdout, temp);

    struct flock fvar;
    int fdesc = open(argv[1], O_RDWR);
    if (fdesc == -1) {
        perror("open");
        return 1;
    }

    lseek(fdesc, -100, SEEK_END);

    fvar.l_type = F_WRLCK;
    fvar.l_whence = SEEK_CUR;
    fvar.l_start = 0;
    fvar.l_len = 100;

    if (fcntl(fdesc, F_SETLK, &fvar) == -1) {
        cout << "\n--------------------\nFile has been locked by:\n";
        while (fcntl(fdesc, F_GETLK, &fvar) != -1 && fvar.l_type != F_UNLCK) {
            cout << "\nFile: " << argv[1] << " is locked by process with pid: " << fvar.l_pid;
            cout << " from " << fvar.l_start << " the byte in the file for: " << fvar.l_len;
            cout << " number of bytes, for " << (fvar.l_type == F_WRLCK ? "write" : "read") << "\n";
            if (!fvar.l_len) break;
            fvar.l_start += fvar.l_len;
            fvar.l_len = 0;
        }
    } else {
        cout << "\n--------------------\n";
        cout << "\n\nFile: " << argv[1] << " was not locked and acquiring of Exclusive lock was successful by Process ID: " << getpid();
        lseek(fdesc, -50, SEEK_END);
        cout << "\n\nLast 50 bytes of file: " << argv[1] << " = \n";

        char buf;
        while (read(fdesc, &buf, 1) > 0) {
            cout << buf;
        }

        lseek(fdesc, -100, SEEK_END);
        fvar.l_type = F_UNLCK;
        fvar.l_whence = SEEK_CUR;
        fvar.l_start = 0;
        fvar.l_len = 100;
        fcntl(fdesc, F_SETLK, &fvar);

        cout << "\nFile unlocked successfully.\n";
    }

    close(fdesc);
    return 0;
}


// OR C CODE 

// #include<stdio.h> 
// #include<sys/types.h> 
// #include<unistd.h> 
// #include<fcntl.h> 
// int main(int argc,char *argv[]){ 
//  char temp[1000]; 
//  setbuf(stdout,temp); 
//  struct flock fvar; 
//  int fdesc,rc; 
//  char buf; 
//  off_t offset; 
//  pid_t pid=fork(); 
//  fdesc=open(argv[1],O_RDWR); 
//  offset=lseek(fdesc,-100,SEEK_END); 
//  fvar.l_type=F_WRLCK; 
//  fvar.l_whence=SEEK_CUR; 
//  fvar.l_start=0; 
//  fvar.l_len=100; 
//  if(fcntl(fdesc,F_SETLK,&fvar)==-1){ 
//   printf("\n--------------------\n File has been locked by:\n"); 
//   while(fcntl(fdesc,F_GETLK,&fvar)!=-1 && fvar.l_type!=F_UNLCK){ 
//    printf("\n File: %s is locked by process with pid: %u",argv[1],fvar.l_pid); 
//    printf(" from %ld the byte in the file for: %ld",fvar.l_start,fvar.l_len); 
//   printf(" number of bytes, for %s\n",(fvar.l_type==F_WRLCK?"write":"read")); 
//    if(!fvar.l_len) break; 
//    fvar.l_start+=fvar.l_len; 
//    fvar.l_len=0; 
//   } 
//  } 
//  else{ 
//   printf("\n--------------------\n"); 
//  printf("\n\n File: %s was not locked and acquiring of Exclusive lock was",argv[1]); 
//   printf(" successful by Process ID: %u",getpid()); 
//   offset=lseek(fdesc,-50,SEEK_END); 
//   printf("\n\n Last 50 bytes of file: %s = \n",argv[1]); 
//   while((rc=read(fdesc,&buf,1))>0) printf("%c",buf); 
//   offset=lseek(fdesc,-100,SEEK_END); 
//   fvar.l_type=F_UNLCK; 
//   fvar.l_whence=SEEK_CUR; 
//   fvar.l_start=0; 
//   fvar.l_len=100; 
//   fcntl(fdesc,F_SETLK,&fvar); 
//   printf("\n File unlocked successfully.\n"); 
//  } 
//  return 0; 
// } 