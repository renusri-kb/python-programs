def fibo(r):
    a=0
    b=1
    for i in range(0,r,1):
        if i<=1:
            n=i
        else:
           n=a+b
           a=b
           b=n
        print(n)
r=int(input())
fibo(r)
