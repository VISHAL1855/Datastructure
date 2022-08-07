#include<iostream>
using namespace std;
int BinarySearch( int arr[],int size,int key)

{
    int start=0;
    int end=size-1;
    int mid=start + (end - start)/2;
    while(start<=end)
    {
        
        if(arr[mid]==key)
        {
            return mid;
        }
        else if (key>start)
        {
            start=mid+1;
        }
        else
        {
            end=mid-1;
        }
        mid=start + (end - start)/2;
    }
    return -1;

}
int main()
{
    int arr[20];
    int size;
    int key,result;
    cout<<"Enter the size of an array:"<<endl;
    cin>>size;
    cout<<"Enter the array elements:"<<endl;
    for(int i=0;i<size;i++)
    {
        cin>>arr[i];
    }
    cout<<"Enter the key you want to search:"<<endl;
    cin>>key;
    result=BinarySearch(arr,size,key);
    cout<<" Key Found at location:"<<result;

}