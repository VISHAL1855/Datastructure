def last(a,si,x):
    l=len(a)
    if si==l:
        return -1
    smaller=last(a,si+1,x)
    if smaller != -1:
        return smaller
    else:
        if a[si]==x:
            return si
        else:
            return -1

def las(a,x):
    l=len(a)
    if l==0:
        return -1
    new=a[1:]
    smaller2=las(new,x)
    if smaller2 ==-1:
        if a[0]==x:
            return 0
        else:
            return -1
    else:
        return smaller2 + 1
        
a=[1,3,4,5,3]
print(las(a,3))
print(last(a,0,3))