def gameOfThrones(s):
    n=len(s)
    count=0
    if n%2==0:
        if any((s.count(i))%2 ==1 for i in s)==True:
            return '1NO'
        return '1YES'
    else:
        s1=set(s)
        for i in s1:
            if s.count(i)%2!=0:
                count+=1
    if count==1:
        return '2YES'
    else:
        return '2NO'

s='aaabbbb' 
print(gameOfThrones(s))
        
    
