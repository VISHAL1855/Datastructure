def factorial(n):
    if n==0:
        return 1
    small=factorial(n-1)
    return n * small

x=int(input("Enter the number whose factorial you want to find:"))
output=factorial(x)
print(output)