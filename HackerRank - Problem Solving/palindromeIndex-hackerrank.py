def palindromeIndex(s):
    if s==s[::-1]:
        return -1
    f=0
    l=len(s)-1
    while(f<l):
        print('f= ',f)
        print('l= ',l)
        if s[f]==s[l]:
            f+=1
            l-=1
            
        elif(s[f]!=s[l]):
            if s[f]==s[l-1]:
                return l
            elif(s[f+1]==s[l]):
                return f
    return -1

s='aabbabaa'
print(palindromeIndex(s))
    
            
