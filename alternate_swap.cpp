#include<iostream>
using namespace std;
void PrintArray(int arr1[],int size)
{
    for(int i=0;i<size;i++)
    {
        cout<<arr1[i]<<" ";
    }
}
void alternate(int arr1[],int size1)
{
    
    for (int i=0;i<size1;i=i+2)
    {
        if(i < i+1)
        {
            swap( arr1[i],arr1[i+1]);
        }
    }
}
int main()
{
    int size=6;int result;
    int arr[100]={1,2,3,4,5,6};
    alternate(arr,size);
    PrintArray(arr,size);


    return 0;

}
