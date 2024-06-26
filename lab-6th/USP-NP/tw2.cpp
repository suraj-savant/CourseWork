#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199303L

#include<iostream>
#include<unistd.h>
using namespace std;

int main()
{
    #ifdef  _POSIX_JOB_CONTROL 
        cout << "_POSIX_JOB_CONTROL is defined"<<endl<<endl;
    #else 
        cout << "Not Defined<<endl"
    #endif

    #ifdef  _POSIX_SAVED_IDS 
        cout << "_POSIX_SAVED_IDS is defined"<<endl;
    #else 
        cout << "Not Defined<<endl"
    #endif

    #ifdef  _POSIX_CHOWN_RESTRICTED 
        cout << "Supports changing file permissons"<<endl;
    #else 
        cout << "Not Defined<<endl"
    #endif

    #ifdef  _POSIX_NO_TRUNC 
        cout << "Supports not truction"<<endl;
    #else 
        cout << "Not Defined<<endl"
    #endif

    #ifdef  _POSIX_VDISABLE 
        cout << "Supports special charactrs"<<endl;
    #else 
        cout << "Not Defined<<endl"
    #endif

    return 0;
}
