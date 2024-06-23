// // Swap adjacent
// #include<iostream>
// using namespace std;

// void print_arrray(int a[], int n)
// {
//   for(int i = 0; i<n; i++)
//   {
//     cout << a[i] << " ";
//   }
// }

// void swap_adjecent(int a[], int n)
// {  
//   int i = 1;
//   int temp;
//   while(i < n)
//   {
//     temp = a[i];
//     a[i] = a[i-1];
//     a[i-1] = temp;
//     i += 2;
//   }
// }

// int main()
// {
//  int n = 5;
//  int a[n] = {1,2,3,4,5};
//  swap_adjecent(a, n);
//  cout << "After swapping " ;
//  print_arrray(a, n);
// }

// // learning about arrays
// #include<iostream>
// using namespace std;

// void printArray(int array[], int size)
// {
//     for(int i=0; i<size; i++)
//         cout << array[i] << " ";
// }

// void takeInput(int array[], int size)
// {
//   for(int i=0; i<size; i++)
//   {
//     cin >> array[i];
//   }
// }

// int max(int array[], int size)
// {
//     int max = INT_MIN;
//     for(int i=0; i<size; i++)
//     {
//         if(array[i]>max)
//            max = array[i];
//     }
//     return max;
// }

// int min(int array[], int size)
// {
//     int min = INT_MAX;
//     for(int i=0; i<size; i++)
//     {
//         if(array[i]<min)
//           min = array[i];
//     }
//     return min;
// }

// int main()
// {
//     int num[10] = {0};
//     takeInput(num, 5);
//     printArray(num, 5);
//     cout << endl;
//     cout << "MIN " << min(num, 5) << endl;
//     cout << "MAX " << max(num, 5) << endl;

// }

// convert array to int
// #include <iostream>
// #include <math.h>
// using namespace std;

// int main()
// {
//     int num[] = {4,5,0};
//     int n = 0, i = 0;
//     int index = 2;
//     while (index >= 0)
//     {
//         int digit = num[index];
//         n = (int(digit) * pow(10, i)) + n;
//         i++;
//         index--;
//     }
//     cout << n;
//     return 0;
// }

// // convert binary to decimal
// #include<iostream>
// #include<math.h>
// using namespace std;

// int main(){
//     uint16_t num = 11;
//     int ans=0, i;
//     while(num != 0)
//     {
//         int digit = num & 1;

//         ans =  digit * pow(2, i) + ans;

//         num = num>>1;
//     }
//     cout << ans;
//     return 0;
// }

// // conversion from decimal to binary
// #include<iostream>
// #include<math.h>
// using namespace std;

// int main()
// {
//     int n;
//     cout << "Enter a number : ";
//     cin >> n;

//     int ans, i =0;
//     while (n != 0)
//     {
//         int bit = n & 1;
//         ans = bit * pow(10, i) + ans;
//         i++;
//         n >>=1;
//     }
//     cout << ans;

// }

// number is even or odd using & operator
//  (a & 1) ? odd : even;
// #include <iostream>
// using namespace std;

// int main()
// {
//     int num;
//     cout << "Enter a number to check even or odd : ";
//     cin >> num;
//     (num & 1) ? cout << "Odd number" : cout << "Even number";
//     return 0;
// }

// // count 1 bits in an number

// #include<iostream>
// using namespace std;

// int main(){
//     uint32_t num = 00010110;
//     int count = 0;

//     while (num != 0)
//     {
//         if(num&1){
//             count++;
//         }
//         num = num >> 1;
//     }

//     cout << "Number of 1 bits " << count << endl;
// }

// // Sum and product of digits

// #include <iostream>
// using namespace std;

// int main()
// {
//     int n = 234;
//     int sum = 0;
//     int product = 1;
//     while (n != 0)
//     {
//         int digit = n % 10;
//         sum += digit;
//         product *= digit;
//         n = n / 10;
//     }
//     cout << "Sum of digits " << sum << endl;
//     cout << "Product of digits " << product;
//     return 0;
// }

// // Prime Number
// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cout << "Enter number to check it prime or not : ";
//     cin >> n;
//     for (int i = 2; i < n; i++)
//     {
//         if(n%i==0){
//             cout << "The number " << n << " is not prime";
//             return 0 ;
//         }
//     }
//     cout << "The number " << n << " is  prime";

//     return 0;
// }

// // Fabonacci series

// #include<iostream>
// using namespace std;

// int main(){
//     int n = 10;
//     int a = 0, b = 1;
//     for(int i = 1; i<=n; i++){
//         int nextFab = a + b;
//         cout << nextFab << " ";
//         a = b;
//         b = nextFab;
//     }
//     return 0;
// }

// #include <iostream>
// using namespace std;

// int main() {
//     // // bitwise operators
//     // int a = 5;
//     // int b = 5;
//     // cout << "a&b " << (a & b) << endl;
//     // cout << "a|b " << (a | b) << endl;
//     // cout << "~a " << (~a) << endl;
//     // cout << "a^b " << (a ^ b) << endl;

//     // // Shift operators
//     // cout << (17 << 1) << endl; // Left shift Multiplies by 2(for each shift) for small nums for large changes sign
//     // cout << (17 >> 1) << endl;  // Left shift divides by 2(for each shift) for small nums for large changes sign
//     // return 0;

//     // // post and pre increment operators

//     // int a = 4, i = 3;
//     // int sum = 4 + (i++);
//     // cout << "a, i, sum : " << a <<" "<< i << " " << sum ;

//     // // op :  a, i, sum : 4 4 7

//     // int a = 4, i = 3;
//     // int sum = 4 + (++i);
//     // cout << "a, i, sum : " << a <<" "<< i << " " << sum ;
// }

// #include <iostream>
// #include<math.h>
// using namespace std;

// int main(int argc, char const *argv[])
// {
// cout << "hello World" << endl;
// for (int i = 0; i < 4; i++)
// {
//     for (int j = 0; j < 4; j++)
//     {
//         cout << j + 1 << "  ";
//     }
//     cout << endl;
// }

// cout << endl
//      << endl;

// int n = 4;
// int i = 0;
// while (i < n)
// {
//     int j =0;
//     while (j < n)
//     {
//         cout << j + 1 << "  ";
//         j++;
//     }
//     cout << endl;
//     i++;
// }

// int count = 4;
// for (int i = 0; i < count; i++)
// {
//     for (int j = 0; j < count; j++)
//     {
//         cout << count - j << "\t";
//     }
//    cout << endl;
// }

// int end_num = 9;
// for (int i = 1; i <= end_num; i++)
// {
//     if(i%3 == 0){
//         cout << i << endl;
//         continue;
//     }
//     cout << i << "  ";
// }

// int n;
// cout << "Enter the count : ";
// cin >> n;
// int count = 1;

// for (int i = 1; i <= n; i++)
// {
//     for (int j = 1; j <= n; j++)
//     {
//         cout << count++ << "  ";
//     }
//     cout << endl;
// }

// int n;
// cout << "Enter number of rows ";
// cin >> n;
// int count = 1;
// for (int i = 1; i <= n; i++)
// {
//     int temp = i;
//     for (int j = 1; j <= i; j++)
//     {
//         cout << temp++ << "  ";
//     }
//     cout << endl;
// }

//     return 0;
// }


#include<iostream>
using namespace std;

bool check_palendrom(string s)
{
    int str_len = s.length();
    for(int i=0; i< str_len /2 ; i++){
        if(s[i] != s[str_len-i -1])
          return false;
    }
    return true;
}

int main(int argc, char const *argv[])
{
    string s = "abbba";
   bool ispalendrome =  check_palendrom(s);
   if(ispalendrome) cout << "YES"; else cout << "NO";
    return 0;
}

