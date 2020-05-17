n=int(input())  #4279
n=str(n)
lar=n[0]    #4            
sml=n[0]    #4
for i in n: #4
    if i>=lar: #4>=4  #2>=4(f)  #7>=4  #9>=7
        lar=i  #lar=4           #lar=7 #lar=9
    elif i<sml:       #2<4   
        sml=i         #sml=2
print(lar,sml)
    
    
