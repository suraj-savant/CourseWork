#include<iostream>
#include<unistd.h>
#include<bits/stdc++.h>

using namespace std;

int main(int argc, const char* argv[]){
    // ln -s main slink
    if(argc == 4 ){
        if(symlink(argv[2], argv[3]) == -1){
            perror("link");
            return 1;
        }
        cout << "Soft link created sucessfully" << endl;
        return 0;
    }

    // ln main hlink
    if(argc == 3){
        if(link(argv[1], argv[2]) == -1){
            perror("link");
            return 1;
        }
        cout << "Hardlink created sucessfully" << endl;
        return 0;
    }

}