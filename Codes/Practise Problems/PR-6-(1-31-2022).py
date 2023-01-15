def merge(lst):
    slst=[]
    for i in lst:
        slst=slst+i
    for x in range(len(slst)):
        for i in range(len(slst[x:])-1):
            if slst[i]>=slst[i+1]:
                temp=slst[i]
                slst[i]=slst[i+1]
                slst[i+1]=temp
    print(slst)
lst=[[0,-1,1],[12,15,20],[17,20,32]] # input
merge(lst)