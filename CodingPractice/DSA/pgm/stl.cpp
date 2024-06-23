// reversing a array
#include<iostream>
#include<vector>

using namespace std;

void printVector(vector<int> arr) {
    for(int i : arr){
        cout << i  << " ";
    }cout<< endl;
}

vector<int> reverse(vector<int> arr)
{
    int start = 0, end = arr.size() - 1;
    while(start < end)
    {
        swap(arr[start++], arr[end--]);
    }
    return arr;
}

int main(int argc, char const *argv[])
{
    vector<int> arr = {10,20,30,40,50,60};
    vector<int> reverseArr;
    printVector(arr);
    reverseArr = reverse(arr);
    printVector(reverseArr);
    return 0;
}


// #include<iostream>
// using namespace std;

// #include<stack>

// int main(int argc, char const *argv[])
// {
//     stack<int> cache;
//     cache.push(10);
//     cache.push(20);
//     cache.push(3);
//     return 0;
// }



// #include<iostream>
// #include<vector>

// using namespace std;


// int main()
// {
//     vector<int> vtr;
//     vtr.push_back(10);
//     vtr.push_back(20);
//     vtr.push_back(30);
//     vtr.push_back(40);
//     vtr.push_back(50);
   
//     cout << "vtr elements : " << endl;
//     for(int i: vtr)
//         cout << " " << i ;
//     cout << endl ;
//     cout << "Print using begin() and end()" << endl;
//     for(auto i=vtr.begin(); i != vtr.end(); ++i)
//     {
//         cout << *i << " ";
//     }

//     cout<<endl;

//     cout << "vtr.size() : " << vtr.size() << endl;
//     cout << "vtr.capacity() : " << vtr.capacity() << endl;
//     cout << "*vtr.begin() : " <<  *vtr.begin() << endl;
//     cout << "*vtr.end() : " << *vtr.end() << endl;


   
    
// }


// #include<iostream>
// #include<vector>
// using namespace std;

// int main()
// {
//     vector<int> myArray = {1,2,3,4,5};
//     for(int i=0; i<myArray.size(); i++)
//     {
//         cout << myArray[i];
//     }
// }

// #include<iostream>
// #include<vector>
// using namespace std;

// void print_vect(vector<int> a)
// {
//     for(int i:a)
//     {
//         cout<< i<< " ";
//     }
// }
// int main()
// {
//     vector<int> vect_a = {1,2,3,4,5};
//     print_vect(vect_a);
//     cout << endl;

//     vector<int> vect_b(vect_a);
//     vect_a[4] = 10;
//     print_vect(vect_a);
//     cout<< endl;
//     print_vect(vect_b);
// }


// #include<iostream>
// #include<vector>
// #include<string>
// using namespace std;

// int main()
// {
//     vector<string> map = {"zero","one", "two", "three", "four", "five", "six"};
//     int num = 450;
//     string  op = "";
//     while(num)
//     {
//         op = map[num%10] + " " + op;
//         num /=10;

//     }

//     cout << op;

// }





