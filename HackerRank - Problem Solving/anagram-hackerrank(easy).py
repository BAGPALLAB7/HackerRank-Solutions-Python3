def anagram(s):
    if len(s)%2!=0:
        return (-1)
    else:
        res=0
        s1=s1=s[:int(len(s)/2)]
        s2=s[int(len(s)/2):]
        s2=list(s2)
        for i in s1:
            if i in s2:
                s2.remove(i)
            else:
                res+=1
    return res

s='ab'
print(anagram(s))
                
        
        
