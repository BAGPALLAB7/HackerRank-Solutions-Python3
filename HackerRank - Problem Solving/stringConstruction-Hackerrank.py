def stringConstruction(s):
    p=[]
    cost=0
    for i in s:
        if i not in p:
            cost+=1
            p.append(i)
    return cost

s='abab'
print(stringConstruction(s))
