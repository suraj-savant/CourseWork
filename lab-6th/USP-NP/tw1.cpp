#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199303L

#include<iostream>
#include<unistd.h>
#include<limits.h>
using namespace std;

int main(){
    int option;
    long res;
    cout << "Enter\n(1) Compile time Congiguration\n(2) Runtime Configuration" << endl;
    cin >> option;

    if(option == 1){
    cout << "Compile time configuaration" << endl;
    cout << "Maximum number of child process " << _POSIX_CHILD_MAX << endl;
    cout << "Maximum number of open files " << _POSIX_OPEN_MAX << endl;
    cout << "Maximum number of characters in path " << _POSIX_PATH_MAX << endl;
    cout << "Maximum characters in filename " << _POSIX_PATH_MAX << endl;
    return 1;
    }

    cout << "Runtime configuration" << endl;
    res = sysconf(_SC_CLK_TCK);
    if(res == -1) 
        cout << "System does not support";
    else
        cout << "Max number of clock cycles " << res << endl;

    res = sysconf(_SC_CHILD_MAX);
    if(res == -1) 
        cout << "System does not support";
    else
        cout << "Max number of child process " << res << endl;



    res = sysconf(_SC_OPEN_MAX);
    if(res == -1) 
        cout << "System does not support";
    else
        cout << "Max number of files opended " << res << endl;



    res = pathconf("/",_PC_PATH_MAX);
    if(res == -1) 
        cout << "System does not support";
    else
        cout << "Max number of path characters " << res << endl;


    res = pathconf("/",_PC_NAME_MAX);
    if(res == -1) 
        cout << "System does not support";
    else
        cout << "Max number of characters in file name " << res << endl;

}