def occurence(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerlist=a[1:]
    smalleroutput=occurence(smallerlist,x)
    if smalleroutput==-1:
        return -1
    else:
        return smalleroutput + 1
def updated(a,si,x):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si
    smallerlist=updated(a,si+1,x)
    return smallerlist

    
a=[1,2,3,4,3,2,3,4,5,4,3]
k=occurence(a,5)
z=updated(a,0,5)
print(z,k)
if z==k:
    print("\nCongratulations both the functions are working fine and have same o/p")
        
    
    

