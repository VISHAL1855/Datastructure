def sorted(a,si):
    l=len(a)
    if si==l or si==l-1:
        return True
    if a[si]> a[si+1]:
        return False 
    small=sorted(a,si+1)
    return small 

a=[1,2,3,4,3,2,4,6]
final=sorted(a,0)
print(final)
