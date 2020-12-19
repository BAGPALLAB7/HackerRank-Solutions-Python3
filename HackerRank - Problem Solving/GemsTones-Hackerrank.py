def gemstones(arr):
    s=arr[0]
    count=0
    new_arr=[]
    for i in arr:
        new_arr.append(list(i))
    for i in range(len(s)):
        flag=0
        for j in range(1,len(new_arr)):
            if (s[i] not in new_arr[j]):
                flag=1
                break
            else:
                new_arr[j].remove(s[i])
        if flag==0:
            count+=1
    return count

arr = ['abcdde', 'baccd', 'eeabg']
print(gemstones(arr))
