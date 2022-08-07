def power(x,n):
    if n==1:
        return x
    smallop=power(x,n-1)
    output=smallop * x
    return output

X=int(input("Enter the Number :"))
Y=int(input("Enter the power to the number :"))
end=power(X,Y)
print(end)

