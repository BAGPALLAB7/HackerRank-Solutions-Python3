def check(c):
    i=0
    jump=0
    while(i<len(c)-1):
        if i<=len(c)-3:
            if c[i+2]!=1:
                i+=2
            else:
                i+=1
            jump+=1
        elif i==len(c)-2:
            if c[i+1]!=1:
                i+=1
                jump+=1
    return jump

arr=[0,1,0 ,1,0, 0 ,1 ,0,1,0,0,0,0,1,0]
print(check(arr))


        
