def utopianTree(n):
    tree=1
    for i in range(1,n+1):
        if i%2!=0:
            tree+=tree
        else:
            tree+=1
    return tree
n=5
print(utopianTree(n))
