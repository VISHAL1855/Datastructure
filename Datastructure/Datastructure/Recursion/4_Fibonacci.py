def fib(n):
    l1=list()
    l2=list()
    if n==1 or n==2:
        return 1
    fib1=fib(n-1)
    fib2=fib(n-2)
    output= fib1+fib2
    return output

n=5
z=fib(n)
print(z)



