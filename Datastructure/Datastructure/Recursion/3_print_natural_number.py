def natural(n):
    if n==0:
        return 
    natural1=natural(n-1)
    print(n)
    return
def natural_rev(n):
    if n==0:
        return
    print(n)
    natural2=natural_rev(n-1)
    return

n=5
natural(n)
natural_rev(n)