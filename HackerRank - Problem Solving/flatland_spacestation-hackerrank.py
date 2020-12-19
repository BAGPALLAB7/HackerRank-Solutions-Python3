n=int(input())
c=[0,1,2,4,3,5]
res=[]
def checkMax(n,stations):
    '''for i in range(n):
        temp=n
        if i in c:
            res.append(0)
        else:
            for j in range(len(c)):
                k=abs(i-c[j])
                if k<=temp:
                    temp=k
                    
            res.append(temp)

    return max(res)'''
    stations = sorted(stations)
    res = stations[0]
    
    for ind in range(1, len(stations)):
        res = max(res, (stations[ind] - stations[ind-1])//2)
        
    res = max(res, n-1 - stations[-1])
        
    return res

result=checkMax(n,c)
print(result)
