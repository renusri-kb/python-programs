def replace(s,n,m):
    r=""
    for i in s:
        if i==n:
            i=m
            r+=i
        else:
            r+=i
    print(r)
s=input("enter a string:")
n=input("char to be replaced:")
m=input("new string:")
replace(s,n,m)

