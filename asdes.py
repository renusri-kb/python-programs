def asdes(n):
    d=0
    a=0
    while n: #n=7281 
        r=n%10 #r=1  8
        n=n//10 #728  72 
        r1=n%10 #r1=8   2
        if r>r1:#1>8 1<8  8>2
            pass
        elif r<r1:
            print("descending order")
            break
        elif r<r1 and r>r1:
            print("mixed")
            break
    else:
        print("ascending order")
n=int(input())
asdes(n)
