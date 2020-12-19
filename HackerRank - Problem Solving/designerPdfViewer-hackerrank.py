def designerPdfViewer(h, word):
    d={}
    l=len(word)
    height=0
    for i in range(len(h)):
        d[chr(97+i)]=h[i]
    for i in word:
        height=max(height,d[i])
    
    return l*height
h=[1 ,3 ,1 ,3 ,1 ,4 ,1 ,3, 2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5, 5, 5, 5, 5 ,5 ,5 ,5 ,5]
word='abc'
print(designerPdfViewer(h,word))
        
    
