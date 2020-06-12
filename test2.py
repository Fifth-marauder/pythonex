comp=pri=tcomp=0
while(1):
    
    m=int(input("Enter the value of m "))
    if(m==-1):
        break
    else:
        for i in range(2,m):
            
            if(m%i==0):
              tcomp=1

           
    if(tcomp==1):
        comp=comp+1
    else:
        pri=pri+1
            
print("The number of prime numbers", pri)
print("The number of composite numbers", comp)

    
