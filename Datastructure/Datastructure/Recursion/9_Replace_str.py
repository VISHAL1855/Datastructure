


def replace(s,a,b):
    if len(s)==0:
        return  s 
    smaller=replace(s[1:],a,b)
    if s[0]==a:
        return b + smaller
    else:
        return s[0]+smaller

s='VSVSVSVSVSVSV'
print(replace(s,"V",'S'))