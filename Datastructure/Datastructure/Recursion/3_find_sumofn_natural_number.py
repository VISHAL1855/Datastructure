def sum1(n):
    if n==1:
        return 1
    small=sum1(n-1)
    out=n + small
    return out

x=int(input("Enter the number upto which you want to find sum:"))
output=sum1(x)
print(output)