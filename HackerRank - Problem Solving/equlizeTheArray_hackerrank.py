def final_check(arr):
    c={}
    count=0
    for i in set(arr):
        c[arr.count(i)]=i
    for i in arr:
        if i!=c[max(c)]:
            count+=1
    return count

arr=[3 ,3 ,2, 1, 3]
print(final_check(arr))
