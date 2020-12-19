def cavityMap(grid):
    new_arr=[]
    for i in range(len(grid)):
        new_arr.append(list(grid[i]))
    
    for i in range(1,len(new_arr)-1):
        for j in range(1,len(new_arr[i])-1):
            if (new_arr[i][j]>new_arr[i-1][j] and new_arr[i][j]>new_arr[i][j-1] and new_arr[i][j]>new_arr[i][j+1] and new_arr[i][j]>new_arr[i+1][j]):
                new_arr[i][j]='X'
    for i in range(len(new_arr)):
        print(new_arr[i])
    grid=[]
    for i in range(len(new_arr)):
        s=''
        for j in range(len(new_arr[i])):
            s+=str(new_arr[i][j])
        grid.append(s)
    for i in range(len(grid)):
        print(grid[i])

arr=['1112','1912','1892','1234']
cavityMap(arr)
    
