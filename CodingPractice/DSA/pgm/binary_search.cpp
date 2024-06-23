#include <iostream>
#include <vector>
using namespace std;

// requires a sorted array as input
// return -1 if element not present in array else returns the index of element
int binarySearch(vector<int> arr, int element)
{
   int begin = 0; int end = arr.size() - 1;
   while (begin <= end )
   {
     int mid = (begin + end) / 2; // s + (e-s) / 2;
     
     if(arr[mid] == element)
        return mid;
     else  if(element < arr[mid])
        end = mid - 1;
    else 
        begin = mid + 1;    
   }
   
   return -1;
}

int firstOcc(vector<int> arr, int element)
{
    int ans = -1;
   int begin = 0; int end = arr.size() - 1;
   while (begin <= end )
   {
     int mid =  begin + (end-begin) / 2;
     
     if(arr[mid] == element)

        return mid;
     else  if(element < arr[mid])
        end = mid - 1;
    else 
        begin = mid + 1;    
   }
   
   return -1;
}




int main(int argc, char const *argv[])
{
    vector<int> arr = {1,2,3,4,5};
    vector<int> pos = left_right_position(arr, 0);
    for(int i=0; i<pos.size(); i++)
     cout << pos[i];

    return 0;
}
