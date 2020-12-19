def makingAnagrams(s1, s2):
    res=0
    s2=list(s2)
    for i in s1:
        if i in s2:
            s2.remove(i)
        else:
            res+=1

    return (res+len(s2))

s1='cde'
s2='abc'
print(makingAnagrams(s1,s2))
