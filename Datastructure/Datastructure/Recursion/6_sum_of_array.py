def sum(a,l):
    if l<=0:
        return 0
    sum1=sum(a,l-1) +a[l-1]
    return sum1

a=[1,3,4]
l=len(a)
new=sum(a,l)
print(new)