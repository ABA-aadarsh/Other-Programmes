def function(lst,k):
    Flag=False
    while lst!=[]:
        t=lst[0]
        lst.remove(t)
        for j in lst:
            if j+t==k:
                print(f"{t}+{j}={k}")
                Flag=True
    if Flag==True:
        return True
    else:
        return False
lst=[1,2,3,4,5,6,7,8,9,10]
k=11
print(function(lst,k))