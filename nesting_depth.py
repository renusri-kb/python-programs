t=int(input())
for i in range(t):
  s=input()
  s2=[]
  s3=[]
  if len(s)==1:
      if int(s)==1:
          s='('+s+')'
          print('case #{}: {}'.format(i+1,s))
  else:    
      for j in range(len(s)):  
       # print(s[j])  
        if j!=len(s)-1:
          if s[j]==s[j+1]:
        #    print(s[j])  
            s2.append(s[j])
            
          else:
            s2.append(s[j])
            s3.append(s2)  
            s2=[]
        else:
          s2.append(s[j])
            
      s3.append(s2)      
      
      s4=''    
      for o in s3:
          
          if str(0) not in o:
              
              s4=s4+'('
              for ol in o:
                 s4=s4+ol
              s4=s4+')'
          else:        
              for l in o:
                  s4=s4+l
      print('case #{}: {}'.format((i+1),s4))            
          
