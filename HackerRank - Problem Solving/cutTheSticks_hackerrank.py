def cutTheSticks(arr):
    res=[]
    while(len(arr)):
        temp=[]
        res.append(len(arr))
        cut=min(arr)
        for i in range(len(arr)):
            arr[i]=arr[i]-cut

        for j in range(len(arr)):
            if arr[j]!=0:
                temp.append(arr[j])
        arr=temp
    return res
arr=[1 ,2 ,3 ,4 ,3 ,3 ,2 ,1]
print(cutTheSticks(arr))
