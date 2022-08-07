#include<iostream>
using namespace std;
int reverse(int arr[],int size )
{
    int a[10];
    for (int i=(size-1);i<=size;i--)
    {
        a[0]= a[0]+ arr[i];

    }
    return arr[0];

}
int main()
{
    int arr[10]={20,4,5,6,23,5,6};
    int size=10;
    cout<<"The reversal array is :"<<reverse( arr,size);
    

}
