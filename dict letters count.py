n="aadityazz"
d={}
count=0
for i in n:
    d[i]=n.count(i)
print(d)
c=max(d.values())
z=[]
for key,values in d.items():
    if values==c:
        z.append(key)
print(max(z),c)
