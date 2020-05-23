def pal(n):
    n=str(n)
    if n==n[::-1]:
        print(n,"palindrome")
    else:
        print(n,"not plindrome")
n=int(input())
pal(n)
