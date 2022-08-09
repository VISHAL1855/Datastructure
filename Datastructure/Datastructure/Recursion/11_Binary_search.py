def Binary_search(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]<x:
        return Binary_search(a,x,mid+1,ei)
    else:
        return  Binary_search(a,x,si,mid-1) 


a=[1,2,3,4,5,6,7,8,9]
si=0
end=len(a)
print(Binary_search(a,6,si,end))