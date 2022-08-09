from dataclasses import replace


def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        small=replace_pi(s[2:])
        return '3.14'+small
    else:
        small=replace_pi(s[1:])
        return s[0] + small

s="abcpianfpidfpi"
print(replace_pi(s))
